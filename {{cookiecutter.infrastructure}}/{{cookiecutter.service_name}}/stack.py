from aws_cdk import core
from vmx_cdk.core import VmxStack

class {{cookiecutter.stack_name}}(VmxStack):
    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        pass # TODO - stack definition goes here
