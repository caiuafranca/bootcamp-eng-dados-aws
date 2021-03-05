#!/usr/bin/env python3

from aws_cdk import core

from aws_cdk_exemplo.aws_cdk_exemplo_stack import AwsCdkExemploStack


app = core.App()
AwsCdkExemploStack(app, "aws-cdk-exemplo")

app.synth()
