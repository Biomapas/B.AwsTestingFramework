from aws_cdk import App

from b_aws_testing_framework_test.tools.testing_with_cdk.infrastructure import Infrastructure

app = App()
Infrastructure(app)
app.synth()
