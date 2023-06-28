import boto3;
from dotenv import load_dotenv;
import os;


def uploadFileToS3():
    load_dotenv()
    access_key = os.getenv('S3_ACCESS_KEY')
    secret_key = os.getenv('S3_SECREY_KEY')
    region = os.getenv('REGION')
    s3_bucket = os.getenv('S3_BUCKET')
    
    session = boto3.Session(
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key,
        region_name=region
    )
    s3 = session.resource('s3')

    # Filename - File to upload
    # Bucket - Bucket to upload to (the top level directory under AWS S3)
    # Key - S3 object name (can contain subdirectories). If not specified then file_name is used
    s3.meta.client.upload_file(Filename='.env', Bucket=s3_bucket, Key='test/.env')




if __name__ == '__main__':
    uploadFileToS3()