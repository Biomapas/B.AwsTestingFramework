from os.path import abspath, dirname

with open(f'{abspath(dirname(__file__))}/../VERSION') as file:
    b_aws_testing_framework_version = file.read()
    b_aws_testing_framework_version = ''.join(b_aws_testing_framework_version.split())
