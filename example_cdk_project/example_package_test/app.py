from aws_cdk.core import App

from example_package_test.infrastructure import Infrastructure

app = App()
Infrastructure(app)
app.synth()
