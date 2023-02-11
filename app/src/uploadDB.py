import boto3
from botocore.exceptions import ClientError
import logging
import csv


def lambda_handler():
    region = 'us-east-1'
    try:
        # get a handle on s3
        session = boto3.Session(region_name=region)
        s3 = session.resource('s3')
        dyndb = boto3.client('dynamodb', region_name=region)
        bucket = s3.Bucket('stock-19281011470')
        obj = bucket.Object(key='test.csv')
        # get the object
        response = obj.get()
        # read the contents of the file
        lines = response['Body'].read().decode('utf-8').splitlines()
        firstrecord = True
        csv_reader = csv.reader(lines, delimiter=';', quotechar='"')
        for row in csv_reader:
            print(row)
            if (firstrecord):
                firstrecord = False
                continue
            code = row[0]
            brand = row[1]
            family = row[2]
            subfamily = row[3]
            model = row[4]
            response = dyndb.put_item(
                TableName='matrix',
                Item={                    # 'S' for type String, 'N' for Number.
                    'code': {'N': code},
                    'brand': {'S': str(brand)},
                    'family': {'S': str(family)},
                    'sub-family': {'S': str(subfamily)},
                    'model': {'S': str(model)}
                }
            )
        result = 'Put succeeded: '
    except ClientError as e:
        logging.error(e)

    return {
        'body': result
    }


lambda_handler()
