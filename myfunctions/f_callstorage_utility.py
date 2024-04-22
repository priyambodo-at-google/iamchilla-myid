from google.cloud import storage
import os
import string
import random
import tempfile
import streamlit as st

@st.cache_resource
def __init__():
    vPROJECT = os.environ.get('GCP_PROJECT')         #Your Google Cloud Project ID
    vREGION = os.environ.get('GCP_REGION')            #Your Google Cloud Project Region
    vBUCKET = os.environ.get('GCP_BUCKET')           #Your Google Cloud Storage Bucket Name
    print("Project ID: " + vPROJECT)
    print("Region: " + vREGION)
    print("Storage Bucket: " + vBUCKET)

#--- Uploading to Google Cloud Storage
def f_createrandomfilename(vFileName):
    """Cleans a filename for compatibility across operating systems.
    Removes spaces, special characters, and limits length to 255 characters.
    Args:
        filename (str): The filename to clean.
    Returns:
        str: The cleaned filename.
    """
    valid_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)
    vFileName = "".join(c for c in vFileName if c in valid_chars)
    vFileName = vFileName.replace(" ", "_")  # Replace spaces with underscores
    vFileName = vFileName[:255]  # Limit length to 255 characters
    vFileName = "chilla_" + str(random.randint(1, 1000000)) + "_" + vFileName
    print (vFileName)
    return vFileName

def f_upload_image_tocloudstorage(vUploadedFile): 
    vBucketName = os.environ.get('GCP_BUCKET')
    vFileName = f_createrandomfilename(vUploadedFile.name)
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        vUploadedFile.seek(0)
        temp_file.write(vUploadedFile.read())
        print(os.path.getsize(temp_file.name))

    storage_client = storage.Client()
    bucket = storage_client.bucket(vBucketName)
    blob = bucket.blob(vFileName)

    if blob.exists():
        vReturn = "File Exists"
        return vReturn
    else:
        try:
            blob.upload_from_filename(temp_file.name)
            os.remove(temp_file.name)
            vReturn = "gs://" + vBucketName + "/" + vFileName
            return vReturn
        except Exception as e:
            print(e)
            return(e)

def f_upload_file_tocloudstorage(vUploadedFile): 
    vBucketName = os.environ.get('GCP_BUCKET')
    vFileName = f_createrandomfilename(vUploadedFile.name)
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        vUploadedFile.seek(0)
        temp_file.write(vUploadedFile.read())
        print(os.path.getsize(temp_file.name))

    storage_client = storage.Client()
    bucket = storage_client.bucket(vBucketName)
    blob = bucket.blob(vFileName)

    if blob.exists():
        vReturn = "File Exists"
        return vReturn
    else:
        try:
            blob.upload_from_filename(temp_file.name)
            os.remove(temp_file.name)
            vReturn = "gs://" + vBucketName + "/" + vFileName
            return vReturn
        except Exception as e:
            print(e)
            return(e)

def f_deletefromcloudstorage(vFileName):
    print("Deleting from Google Cloud Storage: " + vFileName)