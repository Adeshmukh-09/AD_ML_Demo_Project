import logging 
import os
from datetime import datetime

Log_File=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log" ## This is Log_File variable which will be used to create a file with .log ##extension witj current date and time.
log_path=os.path.join(os.getcwd(),"logs",Log_File) ## in thsi variable what it does that if we are working in a specific folder it extract ##that current folder path or directory and create log files for that folder or directory.
os.makedirs(log_path,exist_ok=True) ## this will create a fodler for the logs folder and if that folder exist then skip it.
Log_File_Path=os.path.join(log_path,Log_File) ## this will be the path fo the complete log file.

logging.basicConfig(
    filename=Log_File_Path,
    format="[%(asctime)s]%(lineno)d %(name)s - %(levelname)s - %(message)s", ## this is the format of the log message that we get.
    level=logging.INFO,
)