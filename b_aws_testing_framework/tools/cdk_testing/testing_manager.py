import logging
import os
import sys

from b_continuous_subprocess.continuous_subprocess import ContinuousSubprocess

from b_aws_testing_framework.base_testing_manager import BaseTestingManager
from b_aws_testing_framework.credentials import Credentials
from b_aws_testing_framework.tools.cdk_testing.cdk_tool_config import CdkToolConfig

logger = logging.getLogger(__name__)


class TestingManager(BaseTestingManager):
    """
    Test manager class which prepares infrastructure for tests.
    After tests are finished, destroys the infrastructure.
    """

    def __init__(self, credentials: Credentials, config: CdkToolConfig):
        super().__init__(credentials)

        self.__config = config

        # Ensure that project root is accessible for cdk process.
        if self.__config.project_root_path:
            sys.path.append(self.__config.project_root_path)

        self.__env = {
            **(self.credentials.environ or {}),
            **os.environ.copy(),
            **{'PYTHONPATH': ':'.join(sys.path)}
        }

    def prepare_infrastructure(self) -> None:
        """
        Prepares infrastructure to run tests.
        Firstly, the infrastructure is boot-strapped.
        Secondly, the infrastructure is destroyed (if any leftovers exist).
        Thirdly, the infrastructure is created.

        :return: No return.
        """
        self.set_global_prefix(override=False)
        self.__bootstrap_infrastructure()

        if self.__config.destroy_before_preparing:
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

    def __bootstrap_infrastructure(self) -> None:
        sub = ContinuousSubprocess(TestingManager.__aws_cdk_bootstrap_command())
        output = sub.execute(path=self.__config.cdk_app_path, env=self.__env)
        for line in output: logger.info(line)

    def __create_infrastructure(self) -> None:
        sub = ContinuousSubprocess(TestingManager.__aws_cdk_deploy_command())
        output = sub.execute(path=self.__config.cdk_app_path, env=self.__env)
        for line in output: logger.info(line)

    def __destroy_infrastructure(self) -> None:
        sub = ContinuousSubprocess(TestingManager.__aws_cdk_destroy_command())
        output = sub.execute(path=self.__config.cdk_app_path, env=self.__env)
        for line in output: logger.info(line)

    """
    CDK Commands.
    """

    @staticmethod
    def __aws_cdk_bootstrap_command() -> str:
        return 'cdk bootstrap'

    @staticmethod
    def __aws_cdk_deploy_command() -> str:
        return 'cdk deploy "*" --require-approval never'

    @staticmethod
    def __aws_cdk_destroy_command() -> str:
        return 'cdk destroy "*" --require-approval never --force'
