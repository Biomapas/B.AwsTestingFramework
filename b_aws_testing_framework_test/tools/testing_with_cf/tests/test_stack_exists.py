import logging

from b_aws_testing_framework.credentials import Credentials
from b_aws_testing_framework.tools.cf_testing.testing_manager import TestingManager

logger = logging.getLogger(__name__)


def test_stack_exists() -> None:
    """
    Tests that stack actually was created.

    :return: No return.
    """
    # The stack name is provided by the cf testing manager.
    stack_name = f'{TestingManager.get_global_prefix()}TestStack'

    client = Credentials().boto_session.client('cloudformation')

    stacks = client.list_stacks(StackStatusFilter=['CREATE_COMPLETE'])['StackSummaries']
    stacks = [stack['StackName'] for stack in stacks]

    assert stack_name in stacks
