from os.path import abspath as apat
from os.path import dirname as dirn

from b_aws_testing_framework.credentials import Credentials
from b_aws_testing_framework.tools.cdk_testing.cdk_tool_config import CdkToolConfig
from b_aws_testing_framework.tools.cdk_testing.testing_manager import TestingManager

CDK_PATH = dirn(apat(__file__))
MANAGER = TestingManager(Credentials(), CdkToolConfig(CDK_PATH))


def pytest_configure(*args, **kwargs):
    """
    Called after command line options have been parsed and
    all plugins and initial conftest files been loaded.
    """
    MANAGER.set_global_prefix()
    MANAGER.prepare_infrastructure()


def pytest_unconfigure(*args, **kwargs):
    """
    Called before test process is exited.
    """
    MANAGER.destroy_infrastructure()
