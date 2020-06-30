# BiomapasAwsTest

A python based AWS infrastructure testing micro-framework.<br>
It supports multiple IAC tools like AWS CDK, AWS CloudFormation, and more...

#### Description

Creating infrastructure in AWS is quite hard. There are many nuances,
pitfalls and "gotchas" that sometimes are awfully frustrating. Often some 
IAC code changes might result in some unexpected infrastructure changes.
That is why the created infrastructure should have automated integration tests. 
This python based framework provides you basic functionality to help you
write unit ant integration tests to test AWS infrastructure created
via UI or via tools like AWS CDK. 

The framework is based on pytest - a python based testing library. With that
said, all pytest functionality and configs can be applied on this framework too.

The framework tries to cover some of the most popular IAC tools available on
the market: AWS CDK, Terraform, Troposphere, CloudFormation. More coming...

The framework is easy to use with explicit examples for each IAC tool. Go to
examples section and find which example suits you the most.

#### Remarks

[Biomapas](https://biomapas.com) aims to modernise life-science 
industry by sharing its IT knowledge with other companies and 
the community. This is an open source library intended to be used 
by anyone. Improvements and pull requests are welcome.

#### Related technology

- Python 3
- Pytest
- AWS CDK
- AWS CloudFormation

#### Assumptions

The project assumes the following:

- You have basic-good knowledge in python programming.
- You have basic-good knowledge in AWS.
- You have basic knowledge in testing.

#### Useful sources

- Read more about pytest:<br>
https://docs.pytest.org/en/latest/

#### Install

The project is built and uploaded to PyPi. Install it by using pip.

```bash
pip install biomapas-aws-test
```

Or directly install it through source.

```bash
pip install .
```

#### Examples

- [Testing AWS CDK based projects](https://github.com/Biomapas/BiomapasAwsTest/blob/master/example-cdk.md)
- [Testing CloudFormation based projects](https://github.com/Biomapas/BiomapasAwsTest/blob/master/example-cf.md)
- [Testing Terraform based projects](https://github.com/Biomapas/BiomapasAwsTest/blob/master/example-tf.md)
- [Testing Troposphere based projects](https://github.com/Biomapas/BiomapasAwsTest/blob/master/example-troposphere.md)

#### Testing

The project has tests that can be run. 
Note, that tests are integration tests inherently because they
test how resources are created in AWS environment. Since resources 
are created and tested in AWS you are subject for all the applicable
charges while tests are being run.

##### Setting environment

Before running tests set an environment variable `BIOMAPAS_AWS_TEST_PROFILE`.
This environment variable specifies an aws account to use for deployment and testing.
Usually this profile is called `default` when created with `aws configure` cli command.

Set on Windows:
```bash
set BIOMAPAS_AWS_TEST_PROFILE=default
```

Set on Linux:
```bash
export BIOMAPAS_AWS_TEST_PROFILE=default
```

##### Running tests

Then run tests from a root directory with `pytest` python testing library.

Testing *CloudFormation* functionality:
```bash
pytest biomapas_aws_test_test/tools/testing_with_cf
```

Testing *Cloud Development Kit* functionality:
```bash
pytest biomapas_aws_test_test/tools/testing_with_cdk
```

Testing *Troposphere* functionality:
```bash
pytest biomapas_aws_test_test/tools/testing_with_troposphere
```

Testing *Terraform* functionality:
```bash
pytest biomapas_aws_test_test/tools/testing_with_tf
```

Note that integration tests usually take a while to complete (from 5 to 30
minutes on average).

#### Contribution

Found a bug? Want to add or suggest a new feature?<br>
Contributions of any kind are gladly welcome. You may contact us 
directly, create a pull-request or an issue in github platform.
Lets modernize the world together.
