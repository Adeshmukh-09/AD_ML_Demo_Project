import os ## this we have use because we have to write generic code and it finds out generic folder path to us.
from pathlib import Path ## this specifically helps us to create a path
import logging

logging.basicConfig(level=logging.INFO) ## This will give us the basic and generic logging details.

porject_name="DemoMLProject" ## this is nothing but he name of our project.

list_of_files=[
    f"src/{porject_name}/__init__.py",
    f"src/{porject_name}/components/__init__.py",
    f"src/{porject_name}/components/data_ingestion.py",
    f"src/{porject_name}/components/data_transformation.py",
    f"src/{porject_name}/components/model_trainer.py",
    f"src/{porject_name}/components/data_monitoring.py",
    f"src/{porject_name}/pipelines/__init__.py",
    f"src/{porject_name}/pipelines/training_pipeline.py",
    f"src/{porject_name}/pipelines/prediction_pipeline.py",
    f"src/{porject_name}/exception.py",
    f"src/{porject_name}/logger.py",
    f"src/{porject_name}/utils.py",
    "main.py",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py"
]     

## The meaning of each line in the above list is given here.
## this folder is used in the futrue for the deplloyment purpose because we write some git action for  ##and we write those under workflows ##and .gitkeep is just an indication that we are gonna do something under workflows. (1 line) there was first line but I have deleted it ##for now second line is now the first line in the code.
## this will create a file called as DemoMLProject under the src folder that we have created. (2 line)
## this will create a componenets folder under DemoMLProject folder where we will store our componenets which are  data ingestion, data ##transformation, model training, model monitoring and the components we have created ##below. (3 line)
## the pipelines folders is created in the srrc folder and why we giving __init__.py so that this folder could become a package. (8 line)
## Now what we have done is under pipelines folder we have created two files training and prediction pipeline. (9 and 10 line)
## Now this we have used for the exception handeling for that we are creating another folder. (11 line)


for filepath in list_of_files:               
    filepath= Path(filepath)   ## the variable path that I have used here will find out the relative path from the project.
    filedir, filename=os.path.split(filepath) ## when we write the split code it will give us two info filedir and filenname.

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"creating directory:{filedir} for the file {filename}") ## if the ffiledir is not equal to empty then make the ##filedir.

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0): ## if the path does not exist or the size of the file then we will ##open the file path and we will pass nothhing or append in it and create a looging info which is given there.
        with open(filepath,'w') as f:
            pass
            logging.info(f"creating empty file: {filepath}")
    
    else:
        logging.info(f"{filename} is already exist") ## If the file already exist then this will execute.

                