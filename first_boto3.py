import boto3

s3 = boto3.client('s3')

response = s3.create_bucket(
    Bucket='pnguyen-boto3-06032025'
)
print(response)
