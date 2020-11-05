from aws_cdk.core import Construct

from b_aws_testing_framework.tools.cdk_testing.testing_stack import TestingStack


class TestingInfrastructure(TestingStack):
    """
    This is an entry point for your infrastructure. Create other resources and stacks you want to test here.
    """

    def __init__(self, scope: Construct):
        super().__init__(scope=scope)

        self.add_output('TestKey1', 'TestValue1')
        self.add_output('TestKey2', 'TestValue2')
        self.add_output('TestKey3', 'TestValue3')
