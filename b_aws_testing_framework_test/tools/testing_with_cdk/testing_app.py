from aws_cdk.core import App

# Pycharm complains about this import, however it must be specified exactly like this.
# noinspection PyUnresolvedReferences
from testing_infrastructure import TestingInfrastructure

app = App()
TestingInfrastructure(app)
app.synth()
