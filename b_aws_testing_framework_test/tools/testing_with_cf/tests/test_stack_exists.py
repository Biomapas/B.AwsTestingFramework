import itertools
import logging
from typing import Any, Dict, Iterable

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

    response_iterator = client.get_paginator('list_stacks').paginate(StackStatusFilter=['CREATE_COMPLETE'])
    stack_summaries: Iterable[Dict[str, Any]] = itertools.chain.from_iterable(
        page['StackSummaries'] for page in response_iterator
    )

    stack_names = [stack['StackName'] for stack in stack_summaries]

    assert stack_name in stack_names
