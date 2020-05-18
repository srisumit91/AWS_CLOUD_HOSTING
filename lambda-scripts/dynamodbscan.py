import boto3
from boto3.dynamodb.conditions import Key, Attr
import json

dynamodb = boto3.resource('dynamodb')
table= dynamodb.Table('APIDynamoDBTable')

def lambda_handler(event,context):
##Scanning Complete List Of Records As Below
    response = table.scan()
    
##Checking Count Of Records Before returning Results
    json_response=json.loads(json.dumps(response))
    count=int(str(json_response['Count']))
    
    if (count > 0):
        response = {
              'isBase64Encoded': False,
              'statusCode': 200,
              'headers': {},
              'multiValueHeaders': {},
              'body': str(json.loads(json.dumps(response))['Items'])
            }
    else:
        response = {
              'isBase64Encoded': False,
              'statusCode': 200,
              'headers': {},
              'multiValueHeaders': {},
              'body': 'Corresponding record NotFound'
            }
        
    return response