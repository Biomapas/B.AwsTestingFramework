from biomapas_aws_test.testing_config.testing_config import TestingConfig
from biomapas_aws_test.base_testing_manager import BaseTestingManager
from biomapas_aws_test.tools.testing_with_cdk.testing_manager import TestingManager as CdkTestingManager
from biomapas_aws_test.tools.testing_with_troposphere.testing_manager import TestingManager as TroposphereTestingManager
from biomapas_aws_test.tools.testing_with_cf.testing_manager import TestingManager as CfTestingManager
from biomapas_aws_test.tools.testing_with_tf.testing_manager import TestingManager as TfTestingManager


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

        if TestingConfig.tools_config().get_tf_config():
            return TfTestingManager()

        if TestingConfig.tools_config().get_troposphere_config():
            return TroposphereTestingManager()

        raise ValueError(
            f'Testing method not specified. '
            f'Call {TestingConfig.__name__} to enable one of testing methods.'
        )
