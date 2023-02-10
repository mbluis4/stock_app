"""
import boto3

dynamodb = boto3.resource('dynamodb')

table = dynamodb.create_table(
    TableName='matrix',
    KeySchema=[
        {
            'AttributeName': 'code',
            'KeyType': 'HASH'

        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'id',
            'AttributeType': 'S',
        },
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }

)

table.wait_until_exists()

print(table.item_count)
"""

import boto3
import csv


def lambda_handler(event, context):
    region =’us-east-2'
    try:
        # get a handle on s3
        session = boto3.Session(region_name=region)
        s3 = session.resource(‘s3’)
        dyndb = boto3.client(‘dynamodb’, region_name=region)
        bucket = s3.Bucket(‘YourBucketName’)
        obj = bucket.Object(key=’file.csv’)
        # get the object
        response = obj.get()
        # read the contents of the file
        lines = response[‘Body’].read().decode(‘utf-8’).splitlines()

        firstrecord = True
        csv_reader = csv.reader(lines, delimiter=’, ’, quotechar=’”’)
        for row in csv_reader:
            if (firstrecord):
                firstrecord = False
                continue
            FirstCol = row[0]
            SecondCol = row[1]
            ThirdCol = row[2]
            ForthCol = row[3]
            response = dyndb.put_item(
                TableName=’YourTable’,
                Item={                    # 'S' for type String, 'N' for Number.
                    ‘FirstCol’: {‘S’: str(FirstCol)},
                    ‘SecondCol’: {‘S’: str(SecondCol)},
                    ‘ThirdCol’: {‘S’: str(ThirdCol)},
                    ‘ForthCol’: {‘S’: str(ForthCol)},
                }
            )
        result = ‘Put succeeded: ’
    except Exception as err:
        result = format(err)


return {
    'body': result
}
