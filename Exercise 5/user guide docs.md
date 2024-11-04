Step 1: Create S3 Buckets
1. Create Input S3 Bucket

    - Go to the S3 service in the AWS Management Console.
    - Click on "Create bucket".
    - Name it something like your-input-bucket and configure it as needed (e.g., set the region).
2. Create Output S3 Bucket

    - Follow the same process to create another bucket named your-output-bucket.
      
Step 2: Create Lambda Function to Process the JSON File
Create lambda function by taking the code in same github place.

Step 3: Create the Step Function
1. Go to AWS Step Functions in the Console.
2. Click on "Create state machine".
3. Choose the "Author from scratch" option.
4. Set the state machine name and choose the IAM role.
   
Step 4: Set Up S3 Event Notification to Trigger the Step Function
1. Go to the input S3 bucket.
2. Click on the "Properties" tab.
3. Scroll down to "Event notifications".
4. Click on "Create event notification".
5. Configure the event:
    - Event name: NewFileUpload
    - Event types: Select All object create events.
    - Destination: Choose "Lambda function" and select the Lambda function you created.
6. Save the configuration.

Step 5: Testing the Setup
1. Upload a JSON file to the input S3 bucket. The file should contain an array of objects with name and height attributes, like so:

![image](https://github.com/user-attachments/assets/7bdcfb61-f940-4deb-81d8-3f62cf8384b0)

2. After the upload, the Lambda function should trigger automatically due to the S3 event notification.
3. Check the output S3 bucket. You should see text files named Person1.txt, Person2.txt, etc., containing the respective height information.
