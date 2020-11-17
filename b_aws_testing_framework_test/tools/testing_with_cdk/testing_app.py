from aws_cdk.core import App

"""
Import main stack.
"""

from b_aws_testing_framework_test.tools.testing_with_cdk.testing_infrastructure import TestingInfrastructure

"""
Create CDK app.
"""

app = App()
TestingInfrastructure(app)
app.synth()
