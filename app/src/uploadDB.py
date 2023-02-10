import boto3
from botocore.exceptions import ClientError
import logging

s3 = boto3.client('s3')

response = s3.list_buckets()

for bucket in response['Buckets']:
    print(f' {bucket["Name"]}')
