from functools import lru_cache
from typing import Dict, Optional

from aws_cdk.core import Stack, Construct, CfnOutput

from b_aws_testing_framework.credentials import Credentials
from b_aws_testing_framework.tools.cdk_testing.testing_manager import TestingManager
from b_cf_outputs.cf_outputs import CfOutputs


class TestingStack(Stack):
    """
    A testing stack that can be either inherited or created as an instance.
    Useful for managing outputs.
    """

    def __init__(self, scope: Construct) -> None:
        """
        Constructor.

        :param scope: Parent stack or AWS CDK application.
        """
        self.__scope = scope

        super().__init__(
            scope=scope,
            id=self.name(),
            stack_name=self.name()
        )

    def add_output(self, key: str, value: str) -> None:
        """
        Add an output here so it could be accessed in tests later.

        :param key: Output name.
        :param value: Output value.

        :return: No return.
        """
        CfnOutput(
            scope=self,
            id=key,
            value=value,
            export_name=key
        )

    @staticmethod
    def global_prefix() -> str:
        """
        Returns an already set global prefix.

        :return: Global prefix.
        """
        return TestingManager.get_global_prefix()

    @staticmethod
    def name() -> str:
        """
        Default name of this testing stack.

        :return: Stack name.
        """
        return f'{TestingStack.global_prefix()}TestingStack'

    """
    Methods that should only be used in tests.
    """

    @staticmethod
    def get_output(key: str, credentials: Optional[Credentials] = None) -> str:
        """
        Loads this stack's outputs and creates a corresponding one.

        :param key: Output name (key).
        :param credentials: Optional credentials for AWS API commands.

        :return: Output value.
        """
        return TestingStack.load_outputs_cached(credentials)[key]

    @staticmethod
    @lru_cache(maxsize=None)
    def load_outputs_cached(credentials: Optional[Credentials] = None) -> Dict[str, str]:
        """
        Loads and caches (for better performance) this stack's outputs.

        :param credentials: Optional credentials for AWS API commands.

        :return: All outputs in a form of a dictionary.
        """
        return TestingStack.load_outputs(credentials)

    @staticmethod
    def load_outputs(credentials: Optional[Credentials] = None) -> Dict[str, str]:
        """
        Loads this stack's outputs.

        :param credentials: Optional credentials for AWS API commands.

        :return: All outputs in a form of a dictionary.
        """
        credentials = credentials or Credentials()
        return CfOutputs(credentials.boto_session).get_outputs(TestingStack.name())[TestingStack.name()]
