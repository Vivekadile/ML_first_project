from ML_PROJECT.logger import logging   
from ML_PROJECT.exception import CustomException    
import sys
from ML_PROJECT.components.data_ingestion import DataIngestion
from ML_PROJECT.components.data_ingestion import DataIngestionConfig
from ML_PROJECT.components.data_transformation import DataTransformation, DataTransformationConfig    

if __name__=="__main__":
    logging.info("Starting the ML Project Application")

    try:
        #data_ingestion_config = DataIngestion()
        data_ingestion=DataIngestion()
        data_ingestion.initiate_data_ingestion()
        
        data_transformation = DataTransformation()
        data_transformation.initiate_data_transformation(train_path='artifacts/train.csv', test_path='artifacts/test.csv')

    except Exception as e:
        logging.info("An exception occurred")
        raise CustomException("An error occurred in the main application",sys)