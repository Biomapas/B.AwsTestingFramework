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
from b_aws_testing_framework.testing_config.testing_config import TestingConfig
from b_aws_testing_framework.tools.testing_with_cf.cf_tool_config import CfToolConfig
from b_aws_testing_framework.testing_manager_factory import TestingManagerFactory

def pytest_configure(config):
    TestingConfig.credentials().set_testing_aws_region('eu-central-1')
    TestingConfig.credentials().set_testing_aws_profile('default')
    TestingConfig.tools_config().enable_cf_testing(CfToolConfig('test_stack.yaml'))

def pytest_sessionstart(session):
    TestingManagerFactory.create().prepare_infrastructure()

def pytest_sessionfinish(session, exitstatus):
    TestingManagerFactory.create().destroy_infrastructure()
```

Now create some test, for example:

```python
from b_aws_testing_framework.testing_config.testing_config import TestingConfig

def test_stack_exists() -> None:
    session = boto3.session.Session(
        profile_name=TestingConfig.credentials().get_testing_aws_profile(),
        region_name=TestingConfig.credentials().get_testing_aws_region()
    )

    session.client('cloudformation').list_stacks()
```

If everything looks correct, run in your terminal:

```bash
pytest
```
