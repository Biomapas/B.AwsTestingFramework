import logging
import os

from b_aws_testing_framework.credentials import Credentials
from b_aws_testing_framework.tools.cdk_testing.cdk_tool_config import CdkToolConfig
from b_aws_testing_framework.tools.cdk_testing.testing_manager import TestingManager

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)

CDK_PATH = f'{os.path.dirname(os.path.abspath(__file__))}'


def pytest_sessionstart(session):
    """
    Called after the Session object has been created and
    before performing collection and entering the run test loop.
    """
    TestingManager(Credentials(), CdkToolConfig(CDK_PATH)).prepare_infrastructure()


def pytest_sessionfinish(session, exitstatus):
    """
    Called after whole test run finished, right before
    returning the exit status to the system.
    """
    TestingManager(Credentials(), CdkToolConfig(CDK_PATH)).destroy_infrastructure()
