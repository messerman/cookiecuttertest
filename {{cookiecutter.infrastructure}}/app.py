#!/usr/bin/env python
import os

from aws_cdk import core
from vmx_cdk.core import VmxAccount
from {{cookiecutter.service_name}}.stack import {{cookiecutter.stack_name}}

app = core.App()

tags={
    "PnLGroup": "{{cookiecutter.PnLGroupTag}}",
    "ProductLine": "{{cookiecutter.ProductLineTag}}",
    "Product": "{{cookiecutter.ProductTag}}",
    "Component": "{{cookiecutter.ComponentTag}}",
    "Environment": "{{cookiecutter.EnvironmentTag}}",
    "Customer": "{{cookiecutter.CustomerTag}}",
}

{{cookiecutter.stack_name}}(app, f"{{cookiecutter.stack_name}}", tags=tags)

app.synth()
