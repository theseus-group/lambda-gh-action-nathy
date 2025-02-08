from aws_cdk import (
    Stack,
    CfnOutput,  # ✅ Import CfnOutput properly
    aws_lambda as _lambda,
    aws_apigateway as apigw
)

from constructs import Construct  # ✅ Import Construct separately

class WebAppStack(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)

        # Define Lambda function
        webapp_lambda = _lambda.Function(
            self, "WebAppLambda",
            runtime=_lambda.Runtime.PYTHON_3_8,
            handler="main.lambda_handler",
            code=_lambda.Code.from_asset("app"),
        )

        # API Gateway to expose Lambda function
        api = apigw.LambdaRestApi(
            self, "WebAppAPI",
            handler=webapp_lambda,
            proxy=True,
        )

        # ✅ Corrected CfnOutput usage
        CfnOutput(self, "APIEndpoint", value=api.url)
