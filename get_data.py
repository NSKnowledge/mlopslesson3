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


# import requests
# import zipfile
# import os

# # Define the URL and the destination zip file
# url = 'https://md-datasets-cache-zipfiles-prod.s3.eu-west-1.amazonaws.com/yshdbyj6zy-1.zip'
# zip_name = "data.zip"

# # Download the file using requests
# response = requests.get(url, stream=True)
# if response.status_code == 200:
#     with open(zip_name, 'wb') as f:
#         for chunk in response.iter_content(chunk_size=8192):
#             f.write(chunk)
# else:
#     print(f"Failed to download file: {response.status_code}")

# # Unzip it and standardize the .csv filename
# with zipfile.ZipFile(zip_name, "r") as zip_ref:
#     zip_ref.filelist[0].filename = 'rawdata_new.csv'  # Rename the file inside the zip
#     zip_ref.extract(zip_ref.filelist[0])

# # Clean up by removing the zip file
# os.remove(zip_name)



# import dvc.api
# import os
# import shutil

# # Define the DVC file path (rawdata_new.csv.dvc) and the destination file name
# dvc_file_path = 'rawdata_new.csv.dvc'  # DVC-tracked file
# local_csv_file = 'rawdata_new.csv'  # Name of the file after pulling from DVC
# final_csv_file = 'data_raw.csv'  # Final desired filename

# # Pull the file from DVC remote storage
# # This retrieves the actual file (not the .dvc file) to the local directory
# data = dvc.api.get_dataset(dvc_file_path)

# # Rename the file to 'data_raw.csv' (if necessary)
# if os.path.exists(local_csv_file):
#     os.rename(local_csv_file, final_csv_file)
# else:
#     print(f"Failed to retrieve the file: {local_csv_file}")

# # Optionally, clean up any intermediate files, if needed (e.g., removing the DVC file)
# # os.remove(dvc_file_path)  # Uncomment if you want to delete the .dvc file


import pandas as pd

# Define input and output file names
input_file = 'rawdata_new.csv'
output_file = 'data_raw.csv'

# Read the raw data from the CSV file
try:
    df = pd.read_csv(input_file)
    
    # Perform any necessary transformations if needed
    # For example, let's assume you want to standardize the column names or clean the data
    # (This step is optional depending on your needs)
    
    # Save the data to the new file
    df.to_csv(output_file, index=False)  # index=False to prevent writing row numbers
    
    print(f"File '{input_file}' successfully copied to '{output_file}'.")

except FileNotFoundError:
    print(f"Error: The file '{input_file}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")


