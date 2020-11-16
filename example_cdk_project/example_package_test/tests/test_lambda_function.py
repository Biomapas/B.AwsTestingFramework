import json

from b_aws_testing_framework.credentials import Credentials
from b_aws_testing_framework.tools.cdk_testing.testing_stack import TestingStack
from botocore.response import StreamingBody


def test_lambda_function():
    # Create client for lambda service.
    lambda_client = Credentials().boto_session.client('lambda')

    # Invoke specific lambda function.
    response = lambda_client.invoke(
        FunctionName=TestingStack.get_output('LambdaName'),
        InvocationType='RequestResponse'
    )

    # Parse the result.
    payload: StreamingBody = response['Payload']
    data = [item.decode() for item in payload.iter_lines()]
    data = json.loads(''.join(data))['body']

    # Assert that the result is as expected.
    assert data == 'Hello from lambda function!', data
