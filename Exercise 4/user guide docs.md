Steps to implement a simple REST API using AWS API Gateway and AWS Lambda

Step 1: Create Lambda Functions
Open AWS Console and create two lambda function for GET and POST requests

Step 2: Configure API Gateway
1. Create a new REST API in the AWS API Gateway console.

2. Set up two resources and methods:

    - Resource 1: /greet
        - Method: GET
        - Integration type: Lambda proxy integration
        - Link this to the GET /greet Lambda function.
          
    - Resource 2: /echo
      - Method: POST
      - Integration type: Lambda proxy integration
      - Link this to the POST /echo Lambda function.
        
3. Deploy the API:

    - Create a new stage (e.g., dev) and deploy the API to this stage.
    - Note the endpoint URLs for testing.
