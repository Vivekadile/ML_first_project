## MYsql----> data lunga phir tarin test split karunga 

import os
import sys
from ML_PROJECT.exception import CustomException
from ML_PROJECT.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
 
from dataclasses import dataclass
from ML_PROJECT.utils import read_sql_data

@dataclass
class DataIngestionConfig:
    train_data_path:str=os.path.join('artifacts','train.csv')
    test_data_path:str=os.path.join('artifacts','test.csv')
    raw_data_path:str=os.path.join('artifacts','data.csv')

class DataIngestion:
     def __init__(self):
          self.ingestion_config=DataIngestionConfig()

     def initiate_data_ingestion(self):
          try:
            ##reading the data 
            df=pd.read_csv(os.path.join('notebook','data','data.csv'))
            logging.info("Reading completed from database")
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)
            os.makedirs(os.path.dirname(self.ingestion_config.test_data_path), exist_ok=True)
            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path), exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)
            df.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            df.to_csv(self.ingestion_config.test_data_path,index=False,header=True)
            logging.info("Ingestion of the data is completed")
            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
                   )
          except Exception as e:
               raise CustomException(e, sys)