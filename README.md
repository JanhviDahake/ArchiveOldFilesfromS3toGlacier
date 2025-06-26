# ArchiveOldFilesfromS3toGlacier
Objective: Automate the archival of files older than a certain age from an S3 bucket to Amazon Glacier for cost-effective storage.

Task: Automatically move files in an S3 bucket older than 6 months to Glacier storage class.

Instructions:

1. S3 Setup:

   - Navigate to the S3 dashboard and create a bucket.

   - Upload a mix of old and new files to this bucket.

2. Lambda IAM Role:

   - In the IAM dashboard, create a new role for Lambda.

   - Attach the `AmazonS3FullAccess` policy to this role.

3. Lambda Function:

   - Navigate to the Lambda dashboard and create a new function.

   - Choose Python 3.x as the runtime.

   - Assign the IAM role created in the previous step.

   - Write the Boto3 Python script to:

     1. List objects in the S3 bucket.

     2. Identify files older than 6 months.

     3. Change the storage class of identified files to Glacier.

     4. Log the archived files.

4. Testing:

   - Manually trigger the Lambda function or set it to run periodically.

   - Confirm that older files in the S3 bucket are moved to the Glacier storage class.
