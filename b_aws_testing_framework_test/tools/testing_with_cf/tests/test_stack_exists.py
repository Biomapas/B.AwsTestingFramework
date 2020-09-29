import logging

import boto3

from b_aws_testing_framework.testing_config.testing_config import TestingConfig

logger = logging.getLogger(__name__)


def test_stack_exists() -> None:
    """
    Tests that stack actually was created.

    :return: No return.
    """
    # The stack name is provided by the cf testing manager.
    STACK_NAME = 'TestStack'

    session = boto3.session.Session(
        profile_name=TestingConfig.credentials().get_testing_aws_profile(),
        region_name=TestingConfig.credentials().get_testing_aws_region()
    )

    stacks = session.client('cloudformation').list_stacks(
        StackStatusFilter=['CREATE_COMPLETE']
    )['StackSummaries']
    stacks = [stack['StackName'] for stack in stacks]

    logger.info(f'All available stacks: {stacks}.')

    assert STACK_NAME in stacks
