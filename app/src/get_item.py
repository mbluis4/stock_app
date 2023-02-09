import boto3
import json

dynamodb = boto3.resource('dynamodb')


def lambda_handler(event, context):
    task_id = json.loads(event['body'])['id']

    table = dynamodb.Table('Tasks')

    table.delete_item(
        Key={
            'id': str(task_id)
        }
    )
    return {
        'statusCode': 200,
        'body': json.dumps({
            "message": "task deleted!"
        }),
        'headers': {
            'Content-Type': "application/json",
            'Access-Control-Allow-Origin': '*'
        }

    }


def lambda_handler(event, context):

    dynamodb = boto3.resource('dynamodb')

    table = dynamodb.Table('Tasks')

    response = table.scan()

    return {
        'statusCode': 200,
        'body': json.dumps(response)
    }
