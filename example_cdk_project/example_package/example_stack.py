from aws_cdk.aws_apigateway import LambdaRestApi
from aws_cdk.aws_lambda import Function, Code, Runtime
from aws_cdk.core import Stack


class ExampleStack(Stack):
    def __init__(self, scope: Stack, prefix: str) -> None:
        stack_name = f'{prefix}ExampleStack'
        super().__init__(scope, id=stack_name, stack_name=stack_name)

        lambda_name = f'{prefix}ExampleLambdaFunction'
        self.function = Function(
            scope=self,
            id=lambda_name,
            function_name=lambda_name,
            handler='index.handler',
            runtime=Runtime.PYTHON_3_6,
            code=Code.from_inline(
                'def handler(*args, **kwargs): '
                '    return {'
                '    "isBase64Encoded": False,'
                '    "statusCode": 200,'
                '    "headers": { },'
                '    "body": "Hello from lambda function!"'
                '}'
            )
        )

        api_name = f'{prefix}ExampleRestApi'
        self.api = LambdaRestApi(self, api_name, handler=self.function)
