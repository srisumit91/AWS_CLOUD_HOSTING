import boto3
import json

dynamodb = boto3.resource('dynamodb')
table= dynamodb.Table('APIDynamoDBTable')

def lambda_handler(event,context):
    
    event_dict = json.loads(json.dumps(event))
    event_temp = event_dict['body'].replace('\\',"")
    event_temp = json.loads(event_temp)
    table.put_item(Item=event_temp)
    response = {
              'isBase64Encoded': False,
              'statusCode': 200,
              'headers': {},
              'multiValueHeaders': {},
              'body': 'Record Completely Inserted in DynamoDB'
            }
    return response