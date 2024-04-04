# Google-Cloud-Storage

Sure, here's a content you can add to a README file for your GitHub repository:

```
# Google Cloud Storage Utility

This repository contains a Python class `GoogleCloudStorage` that provides a simple interface
to interact with Google Cloud Storage. The class allows you to create, list, and manage buckets,
as well as upload, download, and delete files in Google Cloud Storage.

## Prerequisites

- Python 3.x
- Google Cloud SDK installed and authenticated
- A Google Cloud Platform project with the Cloud Storage API enabled

## Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/google-cloud-storage-utility.git
```

2. Install the required Python packages:

```bash
pip install google-cloud-storage
```

## Usage

1. Set the `GOOGLE_APPLICATION_CREDENTIALS` environment variable to point to your service account JSON key file:

```python
import os
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'path/to/your/service-account-key.json'
```

2. Import the `GoogleCloudStorage` class and create an instance with an authenticated client:

```python
from google.cloud import storage
from google_cloud_storage_utility import GoogleCloudStorage

storage_client = storage.Client()
gcs = GoogleCloudStorage(storage_client)
```

3. Use the class methods to interact with Google Cloud Storage:

```python
# Create a new bucket
gcs.create_bucket('my-bucket', 'us-central1')

# List all buckets
buckets = gcs.list_buckets()

# Get a bucket object
bucket = gcs.get_bucket('my-bucket')

# Upload a file to the bucket
gcs.upload_file(bucket, 'file.txt', 'path/to/file.txt')

# List all files in the bucket
blobs = gcs.list_blobs('my-bucket')

# Download a file from the bucket
gcs.download_file('my-bucket', 'path/to/download', blob_name='file.txt')

# Delete a file from the bucket
gcs.delete_file(bucket, 'file.txt')
```

## Documentation

The `GoogleCloudStorage` class and its methods are documented using Python docstrings. You can access the documentation by importing the class and calling the `help` function:

```python
from google_cloud_storage_utility import GoogleCloudStorage
help(GoogleCloudStorage)
```

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
```

This README file provides an overview of the project, including prerequisites, installation instructions, usage examples, documentation information, and guidelines for contributing. You can customize it further according to your project's specific requirements.
