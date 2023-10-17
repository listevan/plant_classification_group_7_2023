from io import BytesIO
import os
import zipfile
import requests

def download_zip(url, file_path):
    zip_file_name = url.split("/")[-1]
    file_name = zip_file_name[0:-len('.zip')]
    folder_path = os.path.join(file_path, file_name)
    os.makedirs(folder_path)

    response = requests.get(url)
    with zipfile.ZipFile(BytesIO(response.content)) as zip:
        zip.extractall(folder_path)


    
    