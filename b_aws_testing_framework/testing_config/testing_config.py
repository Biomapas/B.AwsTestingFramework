from b_aws_testing_framework.testing_config.credentials_config import CredentialsConfig
from b_aws_testing_framework.testing_config.tools_config import ToolsConfig


class TestingConfig:
    """
    Main entry point for configuring your testing environment.
    """
    @staticmethod
    def credentials() -> CredentialsConfig:
        return CredentialsConfig()

    @staticmethod
    def tools_config() -> ToolsConfig:
        return ToolsConfig()
