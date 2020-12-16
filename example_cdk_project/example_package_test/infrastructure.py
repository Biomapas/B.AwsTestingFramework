from aws_cdk.core import Construct
from b_aws_testing_framework.tools.cdk_testing.testing_stack import TestingStack

from example_package.example_stack import ExampleStack


class Infrastructure(TestingStack):
    """
    This is an entry point for your infrastructure.
    Create other resources and stacks you want to test here.
    """

    def __init__(self, scope: Construct):
        super().__init__(scope=scope)
        example_stack = ExampleStack(self, self.get_global_prefix())

        self.add_output('LambdaName', example_stack.function.function_name)
        self.add_output('ApiUrl', example_stack.api.url)
