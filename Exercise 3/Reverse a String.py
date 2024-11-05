# This function takes an input string and returns the string reversed.

import json

def lambda_handler(event, context):
    # Extract the input from the event
    input_string = event["input_string"]
    
    if not input_string:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'input_string is required'})
        }
    
    # Reverse the string
    reversed_string = input_string[::-1]
    
    return {
        'statusCode': 200,
        'body': json.dumps({'original': input_string, 'reversed': reversed_string})
    }

