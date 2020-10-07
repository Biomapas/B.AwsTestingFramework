# B.AwsTestingFramework

A python based AWS infrastructure testing micro-framework.<br>
It supports multiple IAC tools like AWS CDK and AWS CloudFormation.

### Description

Creating infrastructure in AWS is quite hard. There are many nuances,
pitfalls and "gotchas" that sometimes are awfully frustrating. Often some 
IAC code changes might result in some unexpected infrastructure changes.
That is why the created infrastructure should have automated integration tests. 
This python based framework provides you basic functionality to help you
write unit ant integration tests to test AWS infrastructure created
via UI or via tools like AWS CDK. 

The framework is based on pytest - a python based testing library. With that
said, all pytest functionality and configs can be applied on this framework too.

The framework is easy to use with explicit examples for each IAC tool. Go to
examples section and find which example suits you the most.

### Remarks

[Biomapas](https://biomapas.com) aims to modernise life-science 
industry by sharing its IT knowledge with other companies and 
the community. This is an open source library intended to be used 
by anyone. Improvements and pull requests are welcome.

### Related technology

- Python 3
- Pytest
- AWS CDK
- AWS CloudFormation

### Assumptions

The project assumes the following:

- You have basic-good knowledge in python programming.
- You have basic-good knowledge in AWS.
- You have basic knowledge in testing.

### Useful sources

- Read more about pytest:<br>
https://docs.pytest.org/en/latest/

### Install

The project is built and uploaded to PyPi. Install it by using pip.

```
pip install b_aws_testing_framework
```

Or directly install it through source.

```
pip install .
```

### Usage & Examples

The framework uses flexible credentials management. You can either
set credentials in the constructor:
```python
from b_aws_testing_framework.credentials import Credentials
Credentials(
    aws_access_key_id='key',
    aws_secret_access_key='secret',
    region_name='region'
)
```

Or you can set the environment:
```
set AWS_ACCESS_KEY_ID=key
set AWS_SECRET_ACCESS_KEY=key
set AWS_DEFAULT_REGION=region
```

And then in your python program:
```python
from b_aws_testing_framework.credentials import Credentials
Credentials()
```

After setting the credentials you can set a `global prefix`. Global prefix
is a globally accessible peace of string that can be used when naming AWS 
resources. This is extremely useful when running tests in CI/CD pipelines
where we can have more than one parallel pipeline running. To access and
manage a global prefix, import your testing manager and use these commands:
```python
# Set a random string.
TestingManager.set_global_prefix()

# Create a resource with a unique name. E.g.
CdkStack(
    scope=scope,
    id=f'{TestingManager.get_global_prefix()}TestingStackId',
    stack_name=f'{TestingManager.get_global_prefix()}TestingStackName'
)
```

See the specific examples for specific tools:

- [Testing AWS CDK based projects](https://github.com/Biomapas/B.AwsTestingFramework/blob/master/documentation/example-cdk.md)
- [Testing CloudFormation based projects](https://github.com/Biomapas/B.AwsTestingFramework/blob/master/documentation/example-cf.md)

### Testing

The project has tests that can be run. 
Note, that tests are integration tests inherently because they
test how resources are created in AWS environment. Since resources 
are created and tested in AWS you are subject for all the applicable
charges while tests are being run.

#### Setting environment

Before running tests set environment variables:
- AWS_ACCESS_KEY_ID
- AWS_SECRET_ACCESS_KEY
- AWS_DEFAULT_REGION

Or:
- AWS_PROFILE
- AWS_DEFAULT_REGION

#### Running tests

Then run tests from a root directory with `pytest` python testing library.

Testing *CloudFormation* functionality:
```
pytest b_aws_testing_framework_test/tools/testing_with_cf
```

Testing *Cloud Development Kit* functionality:
```
pytest b_aws_testing_framework_test/tools/testing_with_cdk
```

Note that integration tests usually take a while to complete (from 5 to 30
minutes on average).

### Contribution

Found a bug? Want to add or suggest a new feature?<br>
Contributions of any kind are gladly welcome. You may contact us 
directly, create a pull-request or an issue in github platform.
Lets modernize the world together.
