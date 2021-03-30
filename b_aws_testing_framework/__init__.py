from os.path import abspath, dirname, basename

import pkg_resources

try:
    with open(f'{abspath(dirname(__file__))}/../VERSION') as file:
        b_aws_testing_framework_version = file.read()
        b_aws_testing_framework_version = ''.join(b_aws_testing_framework_version.split())
except Exception:
    try:
        package_name = basename(dirname(__file__))
        b_aws_testing_framework_version = pkg_resources.get_distribution(package_name).version
    except Exception:
        b_aws_testing_framework_version = 'unspecified'
