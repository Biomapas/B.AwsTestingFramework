from setuptools import setup, find_packages

with open('README.md') as readme_file:
    README = readme_file.read()

with open('HISTORY.md') as history_file:
    HISTORY = history_file.read()

with open('VERSION') as file:
    VERSION = file.read()
    VERSION = ''.join(VERSION.split())

setup(
    name='b_aws_testing_framework',
    version=VERSION,
    license='Apache License 2.0',
    packages=find_packages(exclude=[
        # Exclude virtual environment.
        'venv',
        # Exclude test source files.
        'b_aws_testing_framework_test'
    ]),
    description=(
        'AWS infrastructure testing framework that supports multiple IAC tools.'
    ),
    long_description=README + '\n\n' + HISTORY,
    long_description_content_type='text/markdown',
    include_package_data=True,
    install_requires=[
        'aws-cdk.core>=1.54.0,<2.0.0',
        'boto3>=1.10.46,<1.16.0',
        'pytest>=6.0.2,<7.0.0',
        'b-continuous-subprocess>=0.0.2,<1.0.0',
        'b-cf-outputs>=0.0.3,<1.0.0'
    ],
    author='Laimonas Sutkus',
    author_email='laimonas.sutkus@biomapas.com',
    keywords='AWS Test IAC',
    url='https://github.com/biomapas/B.AwsTestingFramework.git',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
)
