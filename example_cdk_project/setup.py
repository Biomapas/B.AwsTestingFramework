import setuptools


with open("README.md") as fp:
    long_description = fp.read()


setuptools.setup(
    name="example_package",
    version="0.0.1",
    description="An empty CDK Python app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="author",
    package_dir={"": "example_package"},
    packages=setuptools.find_packages(where="example_package"),
    install_requires=[
        "b-aws-testing-framework==0.0.23",
        "aws-cdk.core==1.73.0",
        "aws-cdk.aws-apigateway==1.73.0",
        "aws-cdk.aws-lambda==1.73.0",
    ]
)
