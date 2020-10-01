### Testing infrastructure based on CloudFormation templates

An example file structure of your project could look like this:

```text
- your-project-root             # Project root.
    - package-name/             # Project files.
        - package-file-1.py     # Project file.
        - package-file-2.py     # Project file.
        - package-file-n.py     # Project file.
    - test                      # Testing folder.
        - conftest.py           # Configuring your tests behaviour.
        - test_stack.yaml       # Your CloudFormation template to test.
        - test_stack_exists.py  # Test that asserts the created infrastructure.
    - setup.py                  # Packaging file.
```

Since this framework is based on `pytest` you should create a `conftest.py`
file to configure testing behaviour. The basic contents of the file could
look like this:

```python
from b_aws_testing_framework.credentials import Credentials
from b_aws_testing_framework.tools.cf_testing.cf_tool_config import CfToolConfig
from b_aws_testing_framework.tools.cf_testing.testing_manager import TestingManager


def pytest_sessionstart(session):
    TestingManager(Credentials(), CfToolConfig('.')).prepare_infrastructure()


def pytest_sessionfinish(session, exitstatus):
    TestingManager(Credentials(), CfToolConfig('.')).destroy_infrastructure()

```

Now create some tests, for example:

```python
from b_aws_testing_framework.credentials import Credentials


def test_stack_exists() -> None:
    stacks = Credentials().boto_session.client('cloudformation').list_stacks()['StackSummaries']
    stacks = [stack['StackName'] for stack in stacks]

    assert 'TestStack' in stacks
```

If everything looks correct, run in your terminal:

```
pytest
```
