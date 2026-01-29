from ML_PROJECT.logger import logging   
from ML_PROJECT.exception import CustomException    
import sys

if __name__=="__main__":
    logging.info("Starting the ML Project Application")

    try:
        a=1/0
    except Exception as e:
        logging.info("An exception occurred")
        raise CustomException("An error occurred in the main application",sys)