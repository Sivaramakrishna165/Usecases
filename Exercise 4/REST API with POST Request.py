# This function will handle HTTP POST requests and echo back the JSON data provided in the request body.

import json

def lambda_handler(event, context):
    try:
        # print(event)
        # Extract the JSON body from the event
        body = event
        print(body)
        return {
            'statusCode': 200,
            'body':  body
        }
    except Exception as e:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'Invalid input', 'message': str(e)})
        }
