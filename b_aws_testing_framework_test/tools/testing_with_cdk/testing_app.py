import os
import sys

from os.path import dirname as dn
from aws_cdk.core import App

"""
Import main stack.
"""

sys.path.append(dn(dn(dn(dn(os.path.abspath(__file__))))))
from b_aws_testing_framework_test.tools.testing_with_cdk.testing_infrastructure import TestingInfrastructure

"""
Create CDK app.
"""

app = App()
TestingInfrastructure(app)
app.synth()
