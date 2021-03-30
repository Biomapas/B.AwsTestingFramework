from functools import lru_cache
from typing import Dict, Optional

from aws_cdk.aws_ssm import StringParameter
from aws_cdk.core import Stack, Construct, CfnOutput

from b_aws_testing_framework import b_aws_testing_framework_version
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

        self.b_aws_testing_framework_version_ssm_parameter = StringParameter(
            scope=self,
            id='B.AwsTestingFramework.Version',
            parameter_name='B.AwsTestingFramework.Version',
            string_value=str(b_aws_testing_framework_version)
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
            id=f'{self.global_prefix()}{self.name()}{key}',
            export_name=f'{self.global_prefix()}{key}',
            value=value,
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

    @classmethod
    def get_output(cls, key: str, credentials: Optional[Credentials] = None) -> str:
        """
        Loads this stack's outputs and creates a corresponding one.

        :param key: Output name (key).
        :param credentials: Optional credentials for AWS API commands.

        :return: Output value.
        """
        return cls.load_outputs_cached(credentials)[f'{cls.global_prefix()}{cls.name()}{key}']

    @classmethod
    @lru_cache(maxsize=None)
    def load_outputs_cached(cls, credentials: Optional[Credentials] = None) -> Dict[str, str]:
        """
        Loads and caches (for better performance) this stack's outputs.

        :param credentials: Optional credentials for AWS API commands.

        :return: All outputs in a form of a dictionary.
        """
        return cls.load_outputs(credentials)

    @classmethod
    def load_outputs(cls, credentials: Optional[Credentials] = None) -> Dict[str, str]:
        """
        Loads this stack's outputs.

        :param credentials: Optional credentials for AWS API commands.

        :return: All outputs in a form of a dictionary.
        """
        credentials = credentials or Credentials()
        return CfOutputs(credentials.boto_session).get_outputs(cls.name())[cls.name()]
