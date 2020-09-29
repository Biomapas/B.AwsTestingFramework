import logging

from biomapas_continuous_subprocess.continuous_subprocess import ContinuousSubprocess

from biomapas_aws_test.base_testing_manager import BaseTestingManager
from biomapas_aws_test.testing_config.testing_config import TestingConfig

logger = logging.getLogger(__name__)


class TestingManager(BaseTestingManager):
    """
    Test manager class which prepares infrastructure for tests.
    After tests are finished, destroys the infrastructure.
    """

    def prepare_infrastructure(self) -> None:
        """
        Prepares infrastructure to run tests.
        Firstly, the infrastructure is boot-strapped.
        Secondly, the infrastructure is destroyed (if any leftovers exist).
        Thirdly, the infrastructure is created.

        :return: No return.
        """
        self.__bootstrap_infrastructure()
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
    def __bootstrap_infrastructure() -> None:
        sub = ContinuousSubprocess(TestingManager.__aws_cdk_bootstrap_command())
        output = sub.execute(path=TestingConfig.tools_config().get_cdk_config().cdk_app_path)
        for line in output: logger.info(line)

    @staticmethod
    def __create_infrastructure() -> None:
        sub = ContinuousSubprocess(TestingManager.__aws_cdk_deploy_command())
        output = sub.execute(path=TestingConfig.tools_config().get_cdk_config().cdk_app_path)
        for line in output: logger.info(line)

    @staticmethod
    def __destroy_infrastructure() -> None:
        sub = ContinuousSubprocess(TestingManager.__aws_cdk_destroy_command())
        output = sub.execute(path=TestingConfig.tools_config().get_cdk_config().cdk_app_path)
        for line in output: logger.info(line)

    """
    CDK Commands.
    """

    @staticmethod
    def __aws_cdk_bootstrap_command() -> str:
        profile = TestingConfig.credentials().get_testing_aws_profile()
        profile_arg = f' --profile {profile}' if profile else ''
        command = 'cdk bootstrap' + profile_arg
        return command

    @staticmethod
    def __aws_cdk_deploy_command() -> str:
        profile = TestingConfig.credentials().get_testing_aws_profile()
        profile_arg = f' --profile {profile}' if profile else ''
        command = 'cdk deploy * --require-approval never' + profile_arg
        return command

    @staticmethod
    def __aws_cdk_destroy_command() -> str:
        profile = TestingConfig.credentials().get_testing_aws_profile()
        profile_arg = f' --profile {profile}' if profile else ''
        command = 'cdk destroy * --require-approval never --force' + profile_arg
        return command
