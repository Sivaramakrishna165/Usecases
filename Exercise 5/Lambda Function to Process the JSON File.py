# Lambda function that reads the uploaded JSON file, processes the data, and writes the output to the second S3 bucket.
import json
import boto3
import os

s3_client = boto3.client('s3')

def lambda_handler(event, context):
    # Get bucket name and object key from the event
    input_bucket = event['Records'][0]['s3']['bucket']['name']
    object_key = event['Records'][0]['s3']['object']['key']
    
    # Read the JSON file from S3
    response = s3_client.get_object(Bucket=input_bucket, Key=object_key)
    json_content = json.loads(response['Body'].read())
    
    # Process each item in the JSON array
    for item in json_content:
        name = item.get('name')
        height = item.get('height')
        
        # Prepare content for the text file
        content = f"The height of {name} is {height} cms."
        
        # Create a new text file in the output bucket
        output_key = f"{name}.txt"
        s3_client.put_object(Bucket='your-output-bucket', Key=output_key, Body=content)
    
    return {
        'statusCode': 200,
        'body': json.dumps('Files created successfully!')
    }
