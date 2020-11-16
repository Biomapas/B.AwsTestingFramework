import os

from b_aws_testing_framework.credentials import Credentials
from b_aws_testing_framework.tools.cdk_testing.cdk_tool_config import CdkToolConfig
from b_aws_testing_framework.tools.cdk_testing.testing_manager import TestingManager

CDK_PATH = f'{os.path.dirname(os.path.abspath(__file__))}'


def pytest_configure(*args, **kwargs):
    TestingManager(Credentials(), CdkToolConfig(CDK_PATH)).prepare_infrastructure()


def pytest_unconfigure(*args, **kwargs):
    TestingManager(Credentials(), CdkToolConfig(CDK_PATH)).destroy_infrastructure()
