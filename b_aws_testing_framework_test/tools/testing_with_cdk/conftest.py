import logging
import os

from b_aws_testing_framework.credentials import Credentials
from b_aws_testing_framework.tools.cdk_testing.cdk_tool_config import CdkToolConfig
from b_aws_testing_framework.tools.cdk_testing.testing_manager import TestingManager

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)

CDK_PATH = f'{os.path.dirname(os.path.abspath(__file__))}'


def pytest_configure(*args, **kwargs):
    """
    Called after command line options have been parsed and all plugins and initial conftest files been loaded.
    """
    TestingManager(Credentials(), CdkToolConfig(CDK_PATH)).prepare_infrastructure()


def pytest_unconfigure(*args, **kwargs):
    """
    Called before test process is exited.
    """
    TestingManager(Credentials(), CdkToolConfig(CDK_PATH)).destroy_infrastructure()
