#!/usr/bin/env python
import os

from aws_cdk import core
from vmx_cdk.core import VmxAccount
from {{cookiecutter.service_name}}.stack import {{cookiecutter.stack_name}}

app = core.App()

tags={
    "AccountingCategory": "{{cookiecutter.accounting_category}}",
    "CreatedBy": "{{cookiecutter.creator_username}}",
    "Customer": "{{cookiecutter.customer_name}}",
}

{{cookiecutter.stack_name}}(app, f"{{cookiecutter.stack_name}}", tags=tags)

app.synth()
