import logging
import os
from datetime import datetime


#every time create a new log file , log file name 
LOG_FILE_NAME = f"{datetime.now().strftime('%m%d%Y_%H%M%S')}.log"

# log file directory
LOG_FILE_DIR = os.path.join(os.getcwd(),"logs")

# create a dir of Log Files if not exist
os.makedirs(LOG_FILE_DIR,exist_ok = True)
 
#log file path 
LOG_FILE_PATH = os.path.join(LOG_FILE_DIR,LOG_FILE_NAME)

#logging function : 
logging.basicConfig(
    filename= LOG_FILE_PATH,
    format = " [%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s ",
    level = logging.INFO,
)





