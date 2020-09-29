from typing import Optional

from biomapas_aws_test.tools.testing_with_cdk.cdk_tool_config import CdkToolConfig
from biomapas_aws_test.tools.testing_with_cf.cf_tool_config import CfToolConfig
from biomapas_aws_test.tools.testing_with_tf.tf_tool_config import TfToolConfig
from biomapas_aws_test.tools.testing_with_troposphere.troposphere_tool_config import TroposphereToolConfig


class ToolsConfig:
    __CDK_CONFIG: Optional[CdkToolConfig] = None
    __TF_CONFIG: Optional[TfToolConfig] = None
    __CF_CONFIG: Optional[CfToolConfig] = None
    __TROPOSPHERE_CONFIG: Optional[TroposphereToolConfig] = None

    """
    Cloud Development Kit.
    """

    @staticmethod
    def enable_cdk_testing(config: CdkToolConfig) -> None:
        if any([
            ToolsConfig.__CF_CONFIG,
            ToolsConfig.__TF_CONFIG,
            ToolsConfig.__TROPOSPHERE_CONFIG,
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
            ToolsConfig.__TF_CONFIG,
            ToolsConfig.__TROPOSPHERE_CONFIG,
        ]):
            raise ValueError('Other testing method already enabled.')

        ToolsConfig.__CF_CONFIG = config

    @staticmethod
    def get_cf_config() -> Optional[CfToolConfig]:
        return ToolsConfig.__CF_CONFIG

    """
    Terraform.
    """

    @staticmethod
    def enable_tf_testing(config: TfToolConfig) -> None:
        if any([
            ToolsConfig.__CDK_CONFIG,
            ToolsConfig.__CF_CONFIG,
            ToolsConfig.__TROPOSPHERE_CONFIG,
        ]):
            raise ValueError('Other testing method already enabled.')

        ToolsConfig.__TF_CONFIG = config

    @staticmethod
    def get_tf_config() -> Optional[TfToolConfig]:
        return ToolsConfig.__TF_CONFIG

    """
    Troposphere.
    """

    @staticmethod
    def enable_troposphere_testing(config: TroposphereToolConfig) -> None:
        if any([
            ToolsConfig.__CDK_CONFIG,
            ToolsConfig.__CF_CONFIG,
            ToolsConfig.__TF_CONFIG,
        ]):
            raise ValueError('Other testing method already enabled.')

        ToolsConfig.__TROPOSPHERE_CONFIG = config

    @staticmethod
    def get_troposphere_config() -> Optional[TroposphereToolConfig]:
        return ToolsConfig.__TROPOSPHERE_CONFIG
