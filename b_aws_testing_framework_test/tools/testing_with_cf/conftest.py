import logging
import os
import sys

# Append python package root path so resources could be imported.
# Failing to add these few lines below will result in a "module not found" error.
ROOT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(ROOT_PATH)

from b_aws_testing_framework.testing_config.testing_config import TestingConfig
from b_aws_testing_framework.tools.testing_with_cf.cf_tool_config import CfToolConfig
from b_aws_testing_framework.testing_manager_factory import TestingManagerFactory

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)

STACK_PATH = f'{os.path.dirname(os.path.abspath(__file__))}/test_stack.yaml'


def pytest_configure(config):
    """
    Allows plugins and conftest files to perform initial configuration.
    This hook is called for every plugin and initial conftest
    file after command line options have been parsed.
    """
    TestingConfig.credentials().set_testing_aws_region('eu-central-1')
    TestingConfig.credentials().set_testing_aws_profile(os.environ['BIOMAPAS_AWS_TEST_PROFILE'])
    TestingConfig.tools_config().enable_cf_testing(CfToolConfig(STACK_PATH))


def pytest_sessionstart(session):
    """
    Called after the Session object has been created and
    before performing collection and entering the run test loop.
    """
    TestingManagerFactory.create().prepare_infrastructure()


def pytest_sessionfinish(session, exitstatus):
    """
    Called after whole test run finished, right before
    returning the exit status to the system.
    """
    TestingManagerFactory.create().destroy_infrastructure()


def pytest_unconfigure(config):
    """
    Called before test process is exited.
    """
    pass
