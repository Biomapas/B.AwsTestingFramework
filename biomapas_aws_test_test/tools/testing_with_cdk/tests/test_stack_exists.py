import logging

import boto3

from biomapas_aws_test.testing_config.testing_config import TestingConfig

logger = logging.getLogger(__name__)


def test_stack_exists() -> None:
    """
    Tests that stack actually was created.

    :return: No return.
    """
    # The stack name is provided by the cdk testing infrastructure.
    STACK_NAME = 'TestingStack'

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
