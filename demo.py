from hate.logger import logging
from hate.exception import CustomException
import sys
from hate.configuration.gcloud_syncer import GCloudSync

# logging.info("logging tested")

# try:
#     a = 5/0;
# except Exception as e:
#     raise CustomException(e,sys)

obj = GCloudSync()
obj.sync_folder_from_gcloud("myCreatedBucketName","dataZipFolderName","DataDoenloadFolderLocation")


