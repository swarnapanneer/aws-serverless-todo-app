import json
import boto3
import uuid
from decimal import Decimal

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('todotable')

def lambda_handler(event, context):
    http_method = event['httpMethod']
    
    if http_method == 'POST':
        body = json.loads(event['body'])
        task_id = str(uuid.uuid4())
        item = {
            'taskId': task_id,
            'title': body['title'],
            'completed': False
        }
        table.put_item(Item=item)
        return response(200, item)
    
    elif http_method == 'GET':
        items = table.scan()['Items']
        return response(200, items)
    
    elif http_method == 'PUT':
        body = json.loads(event['body'])
        table.update_item(
            Key={'taskId': body['taskId']},
            UpdateExpression="set completed = :c",
            ExpressionAttributeValues={':c': body['completed']}
        )
        return response(200, {"message": "Updated"})
    
    elif http_method == 'DELETE':
        body = json.loads(event['body'])
        table.delete_item(Key={'taskId': body['taskId']})
        return response(200, {"message": "Deleted"})
    
def response(status, body):
    return {
        "statusCode": status,
        "headers": {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Headers": "*"
        },
        "body": json.dumps(body)
    }