import boto3
from boto3.dynamodb.conditions import Key, Attr
import json

dynamodb = boto3.resource('dynamodb')
table= dynamodb.Table('APIDynamoDBTable')

def lambda_handler(event,context):
##Parsing Request JSON As Below
    annid_temp = json.loads(json.dumps(event))
    annid_temp2=json.loads(json.dumps(annid_temp['queryStringParameters']))
    annid=annid_temp2["annid"].replace("[^a-zA-Z0-9]","")
    
##Querying List Of Records As Below And Finding It Based On Primary Key Of AnnounceId
    response = table.query(
    KeyConditionExpression=Key('AnnounceId').eq(annid)
)
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