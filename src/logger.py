# A log file provides a detailed and easily accessible record of system information that would otherwise be difficult to collate.
# OR
# Any execution that probably happens we should be able to log all those information the execution everything in some files so that will be able to track if there is some errors even the custom exception error we will try to log that into the file.
import logging
import os 
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path = os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

# if __name__=="__main__":
#     logging.info("Logging has started")
