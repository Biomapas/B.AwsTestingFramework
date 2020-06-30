from aws_cdk.core import Stack, CfnOutput


class TestingInfrastructure(Stack):
    def __init__(self, scope: Stack):
        super().__init__(
            scope=scope,
            id='TestingStack',
            stack_name='TestingStack'
        )

        CfnOutput(
            self,
            'TestOutput',
            value='Hello World!',
        )
