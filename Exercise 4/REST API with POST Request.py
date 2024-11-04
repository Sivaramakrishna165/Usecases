# This function will handle HTTP POST requests and echo back the JSON data provided in the request body.

import json

def lambda_handler(event, context):
    try:
        # Extract the JSON body from the event
        body = json.loads(event['body'])
        
        return {
            'statusCode': 200,
            'body': json.dumps({'echo': body})
        }
    except Exception as e:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'Invalid input', 'message': str(e)})
        }
