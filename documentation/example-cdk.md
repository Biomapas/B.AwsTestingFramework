### Testing infrastructure based on AWS CDK

An example file structure of your project could look something like given below. The main idea is two have two 
directories: one for project files and one for testing files.

```text
- your-project-root             # Project root.
    - package-name/             # Project files.
        - package-file-1.py     # Project file.
        - package-file-2.py     # Project file.
        - package-file-n.py     # Project file.
    - test/                     # Testing folder.
        - conftest.py           # Configuring your tests behaviour.
        - test_stack_exists.py  # Test that asserts the created infrastructure.
        - app.py                # AWS CDK app.
        - cdk.json              # AWS CDK configuration.
    - setup.py                  # Packaging file.
```

Since this framework is based on `pytest` you should create a `conftest.py`
file to configure testing behaviour. The basic contents of the file could
look like this:

```python
import os

from b_aws_testing_framework.credentials import Credentials
from b_aws_testing_framework.tools.cdk_testing.cdk_tool_config import CdkToolConfig
from b_aws_testing_framework.tools.cdk_testing.testing_manager import TestingManager

# Usually, your cdk configuration files are going to be in the same directory as the conftest.py file.
# By following an example project structure, the cdk and the root path are:
CDK_PATH = os.path.dirname(os.path.abspath(__file__))
ROOT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def pytest_configure(*args, **kwargs):
    TestingManager(Credentials(), CdkToolConfig(
        cdk_app_path=CDK_PATH,
        project_root_path=ROOT_PATH
    )).prepare_infrastructure()


def pytest_unconfigure(*args, **kwargs):
    TestingManager(Credentials(), CdkToolConfig(
        cdk_app_path=CDK_PATH,
        project_root_path=ROOT_PATH
    )).destroy_infrastructure()
```

The `app.py` file may contain an additional root stack which should be `TestingStack` or at least inherit from it.

```python
from aws_cdk.core import App
from b_aws_testing_framework.tools.cdk_testing.testing_stack import TestingStack

# Initiate CDK applications and synthesize it.
app = App()
TestingStack(app)
app.synth()
```

The `cdk.json` file can remain untouched. Sample file:

```json
{
  "app": "python app.py",
  "context": {
    "@aws-cdk/core:enableStackNameDuplicates": "true",
    "aws-cdk:enableDiffNoFail": "true",
    "@aws-cdk/core:stackRelativeExports": "true"
  }
}
```

Now create some tests, for example:

```python
from b_aws_testing_framework.credentials import Credentials


def test_stack_exists() -> None:
    stacks = Credentials().boto_session.client('cloudformation').list_stacks()['StackSummaries']
    stacks = [stack['StackName'] for stack in stacks]

    assert 'TestStack' in stacks
```

After that, run in your terminal:

```
pytest
```
