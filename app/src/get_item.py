import boto3
import json

dynamodb = boto3.resource('dynamodb')


def lambda_handler(event, context):
    data = json.loads(event)
    print(data)
    item_id = json.loads(event['body'])['code']

    table = dynamodb.Table('matrix')

    response = table.get_item(
        Key={
            'code': item_id
        }
    )
    return {
        'statusCode': 200,
        'body': json.dumps(response),
        'headers': {
            'Content-Type': "application/json",
            'Access-Control-Allow-Origin': '*'
        }

    }


lambda_handler()
