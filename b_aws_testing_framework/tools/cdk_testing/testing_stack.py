from functools import lru_cache
from typing import Dict

from aws_cdk.core import Stack, Construct, CfnOutput

from b_aws_testing_framework.credentials import Credentials
from b_aws_testing_framework.tools.cdk_testing.testing_manager import TestingManager
from b_cf_outputs.cf_outputs import CfOutputs


class TestingStack(Stack):
    def __init__(self, scope: Construct, credentials: Credentials):
        self.__scope = scope
        self.__credentials = credentials

        super().__init__(
            scope=scope,
            id=f'{TestingManager.get_global_prefix()}TestingStack',
            stack_name=f'{TestingManager.get_global_prefix()}TestingStack'
        )

    def add_output(self, key: str, value: str) -> None:
        CfnOutput(
            scope=self,
            id=f'{TestingManager.get_global_prefix()}{key}',
            value=value,
            export_name=key
        )

    # TODO these need to be static for easy access in tests.

    def get_output(self, key: str) -> str:
        return self.load_outputs_cached()[key]

    @lru_cache
    def load_outputs_cached(self) -> Dict[str, str]:
        return self.load_outputs()

    def load_outputs(self) -> Dict[str, str]:
        return CfOutputs(self.__credentials.boto_session).get_outputs(self.stack_name)[self.stack_name]
