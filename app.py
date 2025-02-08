#!/usr/bin/env python3
import aws_cdk as cdk
from infra.cdk_stack import WebAppStack

app = cdk.App()
WebAppStack(app, "WebAppStack")

app.synth()
