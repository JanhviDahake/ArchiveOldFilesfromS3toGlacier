import boto3

s3 = boto3.client('s3')

BUCKET_NAME = 'janhvi-archive-bucket-demo'  # Replace with your bucket name

def lambda_handler(event, context):
    response = s3.list_objects_v2(Bucket=BUCKET_NAME)
    if 'Contents' not in response:
        print("No objects found.")
        return

    archived_files = []

    for obj in response['Contents']:
        key = obj['Key']

        # Get tags for the object
        tagging = s3.get_object_tagging(Bucket=BUCKET_NAME, Key=key)
        tags = {tag['Key']: tag['Value'] for tag in tagging['TagSet']}

        # Check if Archive=true
        if tags.get('Archive', '').lower() == 'true':
            # Archive the object by changing its storage class to Glacier
            s3.copy_object(
                Bucket=BUCKET_NAME,
                Key=key,
                CopySource={'Bucket': BUCKET_NAME, 'Key': key},
                StorageClass='GLACIER',
                MetadataDirective='COPY'
            )
            archived_files.append(key)

    if archived_files:
        print("Archived the following files:")
        for f in archived_files:
            print(f" - {f}")
    else:
        print("No files were tagged for archiving.")
