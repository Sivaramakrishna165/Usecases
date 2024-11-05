# This function takes price and discount and return the result

import json

def lambda_handler(event, context):
    
    # Extract the input from the event
    price = int(event["price"])
    discount = int(event["discount"])
    
    result = price*(1-(discount/100))
    
    return {
        'statusCode': 200,
        'body': json.dumps(result)
    }
