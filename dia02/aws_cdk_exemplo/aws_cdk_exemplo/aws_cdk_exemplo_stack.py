from aws_cdk import 
from aws_cdk import aws_s3 as s3


class AwsCdkExemploStack(core.Stack):

    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        s3.Bucket(self, 'bucket-bootcamp04-test', bucket_name='bucket-bootcamp04-test')
