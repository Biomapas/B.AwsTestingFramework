import logging

from b_aws_testing_framework.credentials import Credentials
from b_aws_testing_framework.tools.cdk_testing.testing_stack import TestingStack

logger = logging.getLogger(__name__)


def test_stack_exists() -> None:
    """
    Tests that stack actually was created.

    :return: No return.
    """
    client = Credentials().boto_session.client('cloudformation')

    stacks = client.list_stacks(StackStatusFilter=['CREATE_COMPLETE'])['StackSummaries']
    stacks = [stack['StackName'] for stack in stacks]

    assert TestingStack.name() in stacks
