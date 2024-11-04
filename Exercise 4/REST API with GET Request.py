# This function will handle HTTP GET requests and return a simple greeting message.

import json

def lambda_handler(event, context):
    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'Hello! Welcome to our API!'})
    }
