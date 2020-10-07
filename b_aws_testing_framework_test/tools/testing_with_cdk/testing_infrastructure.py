from aws_cdk.core import Stack, CfnOutput

from b_aws_testing_framework.tools.cdk_testing.testing_manager import TestingManager


class TestingInfrastructure(Stack):
    def __init__(self, scope: Stack):
        super().__init__(
            scope=scope,
            id=f'{TestingManager.get_global_prefix()}TestingStack',
            stack_name=f'{TestingManager.get_global_prefix()}TestingStack'
        )

        CfnOutput(
            self,
            f'{TestingManager.get_global_prefix()}TestOutput',
            value='Hello World!',
        )
