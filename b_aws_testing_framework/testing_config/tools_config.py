from typing import Optional

from b_aws_testing_framework.tools.testing_with_cdk.cdk_tool_config import CdkToolConfig
from b_aws_testing_framework.tools.testing_with_cf.cf_tool_config import CfToolConfig


class ToolsConfig:
    __CDK_CONFIG: Optional[CdkToolConfig] = None
    __CF_CONFIG: Optional[CfToolConfig] = None

    """
    Cloud Development Kit.
    """

    @staticmethod
    def enable_cdk_testing(config: CdkToolConfig) -> None:
        if any([
            ToolsConfig.__CF_CONFIG,
        ]):
            raise ValueError('Other testing method already enabled.')

        ToolsConfig.__CDK_CONFIG = config

    @staticmethod
    def get_cdk_config() -> Optional[CdkToolConfig]:
        return ToolsConfig.__CDK_CONFIG

    """
    CloudFormation.
    """

    @staticmethod
    def enable_cf_testing(config: CfToolConfig) -> None:
        if any([
            ToolsConfig.__CDK_CONFIG,
        ]):
            raise ValueError('Other testing method already enabled.')

        ToolsConfig.__CF_CONFIG = config

    @staticmethod
    def get_cf_config() -> Optional[CfToolConfig]:
        return ToolsConfig.__CF_CONFIG
