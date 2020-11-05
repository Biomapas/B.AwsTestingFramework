from functools import lru_cache
from typing import Dict, Optional

from aws_cdk.core import Stack, Construct, CfnOutput

from b_aws_testing_framework.credentials import Credentials
from b_aws_testing_framework.tools.cdk_testing.testing_manager import TestingManager
from b_cf_outputs.cf_outputs import CfOutputs


class TestingStack(Stack):
    def __init__(self, scope: Construct):
        self.__scope = scope

        super().__init__(
            scope=scope,
            id=f'{TestingManager.get_global_prefix()}TestingStack',
            stack_name=f'{TestingManager.get_global_prefix()}TestingStack'
        )

    def add_output(self, key: str, value: str) -> None:
        CfnOutput(
            scope=self,
            id=key,
            value=value,
            export_name=key
        )

    @staticmethod
    def name() -> str:
        return f'{TestingManager.get_global_prefix()}TestingStack'

    """
    Methods that should only be used in tests.
    """

    @staticmethod
    def get_output(key: str, credentials: Optional[Credentials] = None) -> str:
        return TestingStack.load_outputs_cached(credentials)[key]

    @staticmethod
    @lru_cache(maxsize=None)
    def load_outputs_cached(credentials: Optional[Credentials] = None) -> Dict[str, str]:
        return TestingStack.load_outputs(credentials)

    @staticmethod
    def load_outputs(credentials: Optional[Credentials] = None) -> Dict[str, str]:
        credentials = credentials or Credentials()
        return CfOutputs(credentials.boto_session).get_outputs(TestingStack.name())[TestingStack.name()]
