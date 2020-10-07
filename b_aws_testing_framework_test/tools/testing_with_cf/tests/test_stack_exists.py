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
    STACK_NAME = f'{TestingManager.get_global_prefix()}TestStack'

    stacks = Credentials().boto_session.client('cloudformation').list_stacks(
        StackStatusFilter=['CREATE_COMPLETE']
    )['StackSummaries']
    stacks = [stack['StackName'] for stack in stacks]

    logger.info(f'All available stacks: {stacks}.')

    assert STACK_NAME in stacks
