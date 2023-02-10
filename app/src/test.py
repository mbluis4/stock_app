import boto3
import logging
from botocore.exceptions import ClientError

s3_client = boto3.client('s3')

try:
    s3_client.create_bucket(Bucket='stock-19281011470')
    print('s3 bucket created')
except ClientError as e:
    logging.error(e)
