# test_aws.py
import boto3

def test_aws_connection():
    s3 = boto3.client('s3')
    response = s3.list_buckets()
    print("S3 Buckets:")
    for bucket in response['Buckets']:
        print(f"  {bucket['Name']}")
    
    ec2 = boto3.client('ec2')
    regions = ec2.describe_regions()
    print("\nAvailable AWS Regions:")
    for region in regions['Regions']:
        print(f"  {region['RegionName']}")

if __name__ == "__main__":
    test_aws_connection()

# import boto3
# from botocore.exceptions import ClientError

# s3 = boto3.client('s3')
# try:
#     s3.create_bucket(
#         Bucket='yair-devops-test-bucket-123456',
#         CreateBucketConfiguration={'LocationConstraint': 'eu-central-1'}
#     )
#     print("✓ Bucket created successfully")
# except ClientError as e:
#     print("✗ Cannot create bucket:", e)
