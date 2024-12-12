# import os
# import wget

# # data from https://www.sciencedirect.com/science/article/pii/S2352340920303048

# # Download the zipped dataset
# url = 'https://md-datasets-cache-zipfiles-prod.s3.eu-west-1.amazonaws.com/yshdbyj6zy-1.zip'
# zip_name = "data.zip"
# wget.download(url, zip_name)

# # Unzip it and standardize the .csv filename
# import zipfile
# with zipfile.ZipFile(zip_name,"r") as zip_ref:
#     zip_ref.filelist[0].filename = 'data_raw.csv'
#     zip_ref.extract(zip_ref.filelist[0])

# os.remove(zip_name)


import requests
import zipfile
import os

# Define the URL and the destination zip file
url = 'https://md-datasets-cache-zipfiles-prod.s3.eu-west-1.amazonaws.com/yshdbyj6zy-1.zip'
zip_name = "data.zip"

# Download the file using requests
response = requests.get(url, stream=True)
if response.status_code == 200:
    with open(zip_name, 'wb') as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)
else:
    print(f"Failed to download file: {response.status_code}")

# Unzip it and standardize the .csv filename
with zipfile.ZipFile(zip_name, "r") as zip_ref:
    zip_ref.filelist[0].filename = 'data_raw.csv'  # Rename the file inside the zip
    zip_ref.extract(zip_ref.filelist[0])

# Clean up by removing the zip file
os.remove(zip_name)

