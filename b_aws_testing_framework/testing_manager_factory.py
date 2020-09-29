from b_aws_testing_framework.testing_config.testing_config import TestingConfig
from b_aws_testing_framework.base_testing_manager import BaseTestingManager
from b_aws_testing_framework.tools.testing_with_cdk.testing_manager import TestingManager as CdkTestingManager
from b_aws_testing_framework.tools.testing_with_cf.testing_manager import TestingManager as CfTestingManager


class TestingManagerFactory:
    """
    Factory class that creates a testing manager based on a global testing configuration.
    """
    @staticmethod
    def create() -> BaseTestingManager:
        """
        Creates testing manager based on global testing configuration.

        :return: Testing manager.
        """
        if TestingConfig.tools_config().get_cdk_config():
            return CdkTestingManager()

        if TestingConfig.tools_config().get_cf_config():
            return CfTestingManager()

        raise ValueError(
            f'Testing method not specified. '
            f'Call {TestingConfig.__name__} to enable one of testing methods.'
        )
