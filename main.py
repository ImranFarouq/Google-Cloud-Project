
from google.cloud import storage
import os

# setting up the environment variable for Google Cloud API Authentication
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'ServiceKey_GoogleCloud.json'

working_dir = os.getcwd()
files_folder = os.path.join(working_dir,'My Files')
downloads_folder = os.path.join(working_dir,'Downloded Files')


class GoogleCloudStorage:
    """
    A class to interact with Google Cloud Storage.

    This class provides methods to create, list, and manage buckets, as well as upload,
    download, and delete files in Google Cloud Storage.

    Attributes:
        client (google.cloud.storage.Client): The authenticated client for interacting with Google Cloud Storage.

    Methods:
        create_bucket(bucket_name, bucket_location): Creates a new bucket with the given name and location.
        list_buckets(): Lists all the buckets associated with the client.
        get_bucket(bucket_name): Retrieves the bucket object with the given name.
        upload_file(bucket, blob_name, file_path): Uploads a file to the specified bucket with the given blob name.
        list_blobs(bucket_name): Lists all the blobs (files) in the specified bucket.
        download_file(bucket_name, download_filepath, all=False, blob_name=None): Downloads a single file or all files from the specified bucket.
        delete_file(bucket, blob_name): Deletes the specified file from the bucket.
    """
    
    def __init__(self, storage_client):
        self.client = storage_client
    
    def create_bucket(self, bucket_name, bucket_location):
        if not bucket_name in self.list_buckets():
            bucket = self.client.bucket(bucket_name)
            bucket.location = bucket_location
            return self.client.create_bucket(bucket)
        else:
            print('Bucket already exists')
            return self.get_bucket(bucket_name)

    def list_buckets(self):
        buckets = self.client.list_buckets()
        return [bucket.name for bucket in buckets]
    
    def get_bucket(self, bucket_name):
        return self.client.get_bucket(bucket_name)
    
    def upload_file(self,bucket, blob_name, file_path):
        blob = bucket.blob(blob_name)
        blob.upload_from_filename(file_path)
        return blob 

    def list_blobs(self, bucket_name):
        return self.client.list_blobs(bucket_name)
    

    def download_file(self,bucket_name, download_filepath, all=False, blob_name=None):
        
        try:
            if all:
                blobs = self.list_blobs(bucket_name)
                for blob in blobs:
                    file_path = os.path.join(download_filepath, blob.name)
                    blob.download_to_filename(file_path)
                print(f"All the Files in the {bucket_name} were Downloaded Successfully")
            
            else:
                bucket = self.get_bucket(bucket_name)
                blob = bucket.blob(blob_name)
                file_path = os.path.join(download_filepath, blob.name)
                blob.download_to_filename(file_path)
                print(f"{blob_name} file was Downloaded Successfully")

        except Exception as e:
            print(e)

    def delete_file(self, bucket, blob_name):
        blob = bucket.blob(blob_name)
        blob.delete()
        print(f"{blob_name} file was Deleted Successfully")

# creating an cloud storage instance
storage_client = storage.Client()

# to Check all available attributes and functions 
# print(dir(storage_client))

gcs = GoogleCloudStorage(storage_client)

bucket_name = 'first_demo_bucket'


# Creating a Bucket or Get the Existing Bucket
if not bucket_name in gcs.list_buckets():
    bucket_gcs = gcs.create_bucket(bucket_name, bucket_location='US')
else:
    print('Bucket already exists')
    bucket_gcs = gcs.get_bucket(bucket_name)


# gives you the details of the bucket
print(vars(bucket_gcs))


# Uploading all the files in My Files Directory 
for filename in os.listdir(files_folder):
    file_path = os.path.join(files_folder, filename)
    blob = gcs.upload_file(bucket=bucket_gcs, blob_name=filename, file_path=str(file_path))
    

# Downloading files from Google Cloud Storage


# Set the Parameter 'all' to True to download all files from the bucket
# We need the Bucket name to list all the blob files in that particular bucket
gcs.download_files(bucket_name='first_demo_bucket', download_filepath = downloads_folder, all=True)

# Download a particular file from Bucket
# Just specify the blob_name parameter which is None by default
 
gcs.download_file(bucket_name='first_demo_bucket', download_filepath = downloads_folder,blob_name='file1.csv')


# Delete a particular file from
gcs.delete_file(bucket=bucket_gcs, blob_name='file1.csv')