import logging

from b_aws_testing_framework.tools.cdk_testing.testing_stack import TestingStack

logger = logging.getLogger(__name__)


def test_outputs() -> None:
    """
    Tests that outputs were created.

    :return: No return.
    """
    assert TestingStack.get_output('TestKey1') == 'TestValue1'
    assert TestingStack.get_output('TestKey2') == 'TestValue2'
    assert TestingStack.get_output('TestKey3') == 'TestValue3'
