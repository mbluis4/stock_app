
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

# for key, value in df.items():
#    print(key, value)
