Explanation of the CloudFormation Template
1. Parameters: You can specify the names of the input and output S3 buckets during stack creation.
2. Resources:
    - S3 Buckets: Defines the input and output buckets.
    - IAM Roles: Creates roles for Lambda functions and Step Functions with necessary permissions.
    - Lambda Functions: Creates Lambda functions for the REST API (GET /greet and POST /echo) and for processing JSON files uploaded to S3.
    - API Gateway: Sets up API Gateway resources and methods for the Lambda functions.
    - Step Functions: Defines a Step Function that invokes the processing Lambda function.
3. Outputs: Provides the URL for the deployed API Gateway.

Deployment Instructions
1. Save the above template to a file named template.yaml.
2. Use the AWS CLI to create the CloudFormation stack
   
   aws cloudformation create-stack --stack-name MyStack --template-body file://template.yaml --parameters ParameterKey=InputBucketName,ParameterValue=your-input-bucket ParameterKey=OutputBucketName,ParameterValue=your-output-bucket --capabilities CAPABILITY_IAM
4. Wait for the stack creation to complete.
