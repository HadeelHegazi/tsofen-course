import logging
import boto3
from botocore.exceptions import ClientError
import os



def create_bucket(bucket_name, region=None):
    # Create bucket
    try:
        if region is None:
            s3_client = boto3.client('s3')
            s3_client.create_bucket(Bucket=bucket_name)
        else:
            s3_client = boto3.client('s3', region_name=region)
            location = {'LocationConstraint': region}
            s3_client.create_bucket(Bucket=bucket_name,
                                    CreateBucketConfiguration=location)
    except ClientError as e:
        logging.error(e)
        return False
    return True


def get_bucket_list(region=None):

    # Retrieve the list of existing buckets
    s3 = boto3.client('s3')
    response = s3.list_buckets()

    # Output the bucket names
    print('Existing buckets:')
    for bucket in response['Buckets']:
        print(f'  {bucket["Name"]}')

def upload_file(file_name, bucket, object_name=None):

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = os.path.basename(file_name)

    # Upload the file
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True

def dow_file(bucket_name, object_name, file_name):

    s3 = boto3.client('s3')
    s3.download_file(bucket_name, object_name, file_name)


create_bucket('testbucket1')
get_bucket_list()
upload_file('/home/osboxes/Documents/aws/toS','hadelbuckettest')
dow_file('hadelbuckettest','toS','/home/osboxes/Documents/aws/toSdow')