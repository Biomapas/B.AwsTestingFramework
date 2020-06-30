from biomapas_aws_test.testing_config.credentials_config import CredentialsConfig
from biomapas_aws_test.testing_config.tools_config import ToolsConfig


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
