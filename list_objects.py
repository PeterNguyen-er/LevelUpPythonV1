import boto3

s3 = boto3.client('s3')

response = s3.list_objects_v2(Bucket='pnguyen-boto3-06032025') # response = s3.list_objects_v2(Bucket='pnguyen-boto3-06032025', Prefix="folder/folder_a") # search in specific folder "folder_a" in this case

for content in response["Contents"]:
# filtering out search example # if(".txt" in content["Key"][-4:]): # this will only search the last four(.txt) of the file; must adjust number to type of file.
    print(content["Key"])
    