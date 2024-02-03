from src.DemoMLProject.logger import logging 
from src.DemoMLProject.exception import CustomException
import sys



if __name__=="__main__":
    logging.info("execution has started")

    try:
        a=1/0
    except Exception as e:
        logging.info("custom Exception")
        raise CustomException(e,sys)


 