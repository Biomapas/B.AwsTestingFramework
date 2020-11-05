import logging

from botocore.exceptions import ClientError

from b_aws_testing_framework.base_testing_manager import BaseTestingManager
from b_aws_testing_framework.credentials import Credentials
from b_aws_testing_framework.tools.cf_testing.cf_tool_config import CfToolConfig
from b_aws_testing_framework.tools.cf_testing.stack_waiter import StackWaiter

logger = logging.getLogger(__name__)


class TestingManager(BaseTestingManager):
    """
    Test manager class which prepares infrastructure for tests.
    After tests are finished, destroys the infrastructure.
    """

    def __init__(self, credentials: Credentials, config: CfToolConfig):
        super().__init__(credentials)

        self.__config = config

    def prepare_infrastructure(self) -> None:
        """
        Prepares infrastructure to run tests.
        Firstly, the infrastructure is destroyed (if any leftovers exist).
        Secondly, the infrastructure is created.

        :return: No return.
        """
        self.set_global_prefix(override=False)
        self.__destroy_infrastructure()
        self.__create_infrastructure()

    def destroy_infrastructure(self) -> None:
        """
        Destroys the infrastructure.
        
        :return: No return.
        """
        self.__destroy_infrastructure()
        self.delete_global_prefix()

    """
    Infrastructure functions.
    """

    def __create_infrastructure(self) -> None:
        client = self.credentials.boto_session.client('cloudformation')

        with open(self.__config.cf_template_path, 'r') as file:
            client.create_stack(
                StackName=f'{self.get_global_prefix()}TestStack',
                TemplateBody=file.read(),
                Capabilities=['CAPABILITY_IAM'],
            )

        StackWaiter(f'{self.get_global_prefix()}TestStack').wait()

    def __destroy_infrastructure(self) -> None:
        client = self.credentials.boto_session.client('cloudformation')

        try:
            client.delete_stack(
                StackName=f'{self.get_global_prefix()}TestStack',
            )
        except ClientError as ex:
            # Retrieve code and message from an error.
            code = ex.response['Error']['Code']
            message = ex.response['Error']['Message']

            # If stack does not exist, its fine, just return None.
            if code == 'ValidationError' and 'does not exist' in message.lower():
                return

            # Otherwise throw an exception.
            raise

        StackWaiter(f'{self.get_global_prefix()}TestStack').wait()
