from setuptools import setup, find_packages

with open('README.md') as readme_file:
    README = readme_file.read()

with open('HISTORY.md') as history_file:
    HISTORY = history_file.read()

setup(
    name='b_aws_testing_framework',
    version='0.0.4',
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
    long_description_content_type="text/markdown",
    include_package_data=True,
    install_requires=[
        "pytest>=5.4.3,<6.0.0",
        "biomapas-continuous-subprocess>=1.0.0,<2.0.0"
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
