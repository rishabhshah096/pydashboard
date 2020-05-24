import boto3
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Music')
print(table.creation_date_time)

response = table.get_item(
    Key={
        'Artist': 'No One You Know',
        'songTitle': 'Call Me Today'
    }
)
item = response['Item']
print(item)
print(item['songTitle'])
