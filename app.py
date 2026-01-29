from ML_PROJECT.logger import logging   
from ML_PROJECT.exception import CustomException    
import sys
from ML_PROJECT.components.data_ingestion import DataIngestion
from ML_PROJECT.components.data_ingestion import DataIngestionConfig
        

if __name__=="__main__":
    logging.info("Starting the ML Project Application")

    try:
        #data_ingestion_config = DataIngestion()
        data_ingestion=DataIngestion()
        data_ingestion.initiate_data_ingestion()

    except Exception as e:
        logging.info("An exception occurred")
        raise CustomException("An error occurred in the main application",sys)