import logging
import os
import sys
from typing import Any, Optional, Callable

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

        # Additional process environment context.
        __additional_env = {
            **(self.credentials.environ or {}),
            **os.environ.copy(),
            **{'PYTHONPATH': ':'.join(sys.path)}
        }

        # Update the config environment with additional process environment context.
        for key, value in __additional_env.items():
            if config.deployment_process_environment.get(key) is None:
                config.deployment_process_environment[key] = value

    def prepare_infrastructure(self, custom_deploy_action: Optional[Callable[[CdkToolConfig], Any]] = None) -> None:
        """
        Prepares infrastructure to run tests.
        Firstly, the infrastructure is boot-strapped.
        Secondly, the infrastructure is destroyed (if any leftovers exist).
        Thirdly, the infrastructure is created.

        :param custom_deploy_action: Read more about this parameter in parent class.

        :return: No return.
        """
        logger.info('Setting global prefix (not overriding an existing one)...')
        self.set_global_prefix(override=False)

        logger.info('Bootstrapping the infrastructure...')
        self.__bootstrap_infrastructure()

        if self.__config.destroy_before_preparing:
            logger.info('Destroying the infrastructure before creating a new one...')
            self.__destroy_infrastructure()

        if custom_deploy_action:
            custom_deploy_action(self.__config)
        else:
            self.__create_infrastructure()

    def destroy_infrastructure(self, custom_destroy_action: Optional[Callable[[CdkToolConfig], Any]] = None) -> None:
        """
        Destroys the infrastructure.

        :param custom_destroy_action: Read more about this parameter in parent class.

        :return: No return.
        """
        if custom_destroy_action:
            custom_destroy_action(self.__config)
        else:
            self.__destroy_infrastructure()

        self.delete_global_prefix()

    """
    Infrastructure functions.
    """

    def __bootstrap_infrastructure(self) -> None:
        sub = ContinuousSubprocess(self.__aws_cdk_bootstrap_command())
        output = sub.execute(path=self.__config.cdk_app_path, env=self.__config.deployment_process_environment)
        for line in output: logger.info(line.strip())

    def __create_infrastructure(self) -> None:
        sub = ContinuousSubprocess(self.__aws_cdk_deploy_command())
        output = sub.execute(path=self.__config.cdk_app_path, env=self.__config.deployment_process_environment)
        for line in output: logger.info(line.strip())

    def __destroy_infrastructure(self) -> None:
        sub = ContinuousSubprocess(self.__aws_cdk_destroy_command())
        output = sub.execute(path=self.__config.cdk_app_path, env=self.__config.deployment_process_environment)
        for line in output: logger.info(line.strip())

    """
    CDK Commands.
    """

    def __aws_cdk_bootstrap_command(self) -> str:
        return f'cdk bootstrap aws://{self.credentials.aws_account_id}/{self.credentials.region_name}'

    @classmethod
    def __aws_cdk_deploy_command(cls) -> str:
        return f'cdk deploy --all --require-approval never'

    @classmethod
    def __aws_cdk_destroy_command(cls) -> str:
        return f'cdk destroy --all --require-approval never --force'
