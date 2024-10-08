import requests
import tempfile
import boto3

def download_http(wurl):
    # Append "https://data.commoncrawl.org/" to the wurl
    wurl = "https://data.commoncrawl.org/" + wurl

    # Send a GET request to the wurl and save the response to a Response object
    r = requests.get(wurl, stream=True)

    # Create a temporary file to store the response data
    f = tempfile.TemporaryFile()

    # Write the response data to the temporary file in chunks
    for chunk in r.iter_content(chunk_size=8192):
        f.write(chunk)

    # Seek back to the beginning of the file so it can be read
    f.seek(0)

    # Read the entire contents of the file and return it
    return f.read()



def downls_s3(wurl):
    s3client = boto3.client('s3', use_ssl=False)
    data = tempfile.TemporaryFile()
    s3client.download_fileobj(
    'commoncrawl',
    wurl,
    data
    )
    data.seek(0)
    return data