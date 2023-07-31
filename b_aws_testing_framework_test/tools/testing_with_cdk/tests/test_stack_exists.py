import itertools
import logging
from typing import Iterable, Dict, Any

from b_aws_testing_framework.credentials import Credentials
from b_aws_testing_framework.tools.cdk_testing.testing_stack import TestingStack

logger = logging.getLogger(__name__)


def test_stack_exists() -> None:
    """
    Tests that stack actually was created.

    :return: No return.
    """
    client = Credentials().boto_session.client('cloudformation')

    response_iterator = client.get_paginator('list_stacks').paginate(StackStatusFilter=['CREATE_COMPLETE'])
    stack_summaries: Iterable[Dict[str, Any]] = itertools.chain.from_iterable(
        page['StackSummaries'] for page in response_iterator
    )

    stack_names = [stack['StackName'] for stack in stack_summaries]

    assert TestingStack.name() in stack_names
