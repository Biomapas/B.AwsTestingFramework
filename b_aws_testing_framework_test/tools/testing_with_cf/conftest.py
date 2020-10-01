import logging
import os
import sys

# Append python package root path so resources could be imported.
# Failing to add these few lines below will result in a "module not found" error.
ROOT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(ROOT_PATH)

from b_aws_testing_framework.credentials import Credentials
from b_aws_testing_framework.tools.cf_testing.cf_tool_config import CfToolConfig
from b_aws_testing_framework.tools.cf_testing.testing_manager import TestingManager

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)

STACK_PATH = f'{os.path.dirname(os.path.abspath(__file__))}/test_stack.yaml'


def pytest_sessionstart(session):
    """
    Called after the Session object has been created and
    before performing collection and entering the run test loop.
    """
    TestingManager(Credentials(), CfToolConfig(STACK_PATH)).prepare_infrastructure()


def pytest_sessionfinish(session, exitstatus):
    """
    Called after whole test run finished, right before
    returning the exit status to the system.
    """
    TestingManager(Credentials(), CfToolConfig(STACK_PATH)).destroy_infrastructure()
