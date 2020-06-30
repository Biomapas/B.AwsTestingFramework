import logging

import boto3 as boto3
from botocore.exceptions import ClientError

from biomapas_aws_test.base_testing_manager import BaseTestingManager
from biomapas_aws_test.testing_config.testing_config import TestingConfig
from biomapas_aws_test.tools.testing_with_cf.stack_waiter import StackWaiter

logger = logging.getLogger(__name__)


class TestingManager(BaseTestingManager):
    """
    Test manager class which prepares infrastructure for tests.
    After tests are finished, destroys the infrastructure.
    """

    def prepare_infrastructure(self) -> None:
        """
        Prepares infrastructure to run tests.
        Firstly, the infrastructure is destroyed (if any leftovers exist).
        Secondly, the infrastructure is created.

        :return: No return.
        """
        self.__destroy_infrastructure()
        self.__create_infrastructure()

    def destroy_infrastructure(self) -> None:
        """
        Destroys the infrastructure.
        
        :return: No return.
        """
        self.__destroy_infrastructure()

    """
    Infrastructure functions.
    """

    @staticmethod
    def __create_infrastructure() -> None:
        client = boto3.session.Session(
            profile_name=TestingConfig.credentials().get_testing_aws_profile(),
            region_name=TestingConfig.credentials().get_testing_aws_region()
        ).client('cloudformation')

        with open(TestingConfig.tools_config().get_cf_config().cf_template_path, 'r') as file:
            client.create_stack(
                StackName='TestStack',
                TemplateBody=file.read(),
                Capabilities=['CAPABILITY_IAM'],
            )

        StackWaiter('TestStack').wait()

    @staticmethod
    def __destroy_infrastructure() -> None:
        client = boto3.session.Session(
            profile_name=TestingConfig.credentials().get_testing_aws_profile(),
            region_name=TestingConfig.credentials().get_testing_aws_region()
        ).client('cloudformation')

        try:
            client.delete_stack(
                StackName='TestStack',
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

        StackWaiter('TestStack').wait()
