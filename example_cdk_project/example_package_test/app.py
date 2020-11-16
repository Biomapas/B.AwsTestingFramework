from aws_cdk.core import App
from b_aws_testing_framework.tools.cdk_testing.testing_stack import TestingStack
from b_aws_testing_framework.tools.cdk_testing.testing_manager import TestingManager

import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from example_package.example_stack import ExampleStack

app = App()

stack = TestingStack(app)

example_stack = ExampleStack(stack, TestingManager.get_global_prefix())

stack.add_output('LambdaName', example_stack.function.function_name)
stack.add_output('ApiUrl', example_stack.api.url)

app.synth()
