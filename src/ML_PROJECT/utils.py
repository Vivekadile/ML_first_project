import os 
import sys

from flask import logging
from ML_PROJECT.exception import CustomException
from ML_PROJECT.logger import logging
import pandas as pd
from dotenv import load_dotenv  
import pymysql
from ML_PROJECT.utils import read_sql_data

load_dotenv()
host=os.getenv("host")
user=os.getenv("user")
password=os.getenv("password")
database=os.getenv("database")
db=os.getenv('db')

def read_sql_data():
    logging.info("Reading data from MySQL database")
    try:
        mydb=pymysql.connect(

            host=host,
            user=user,
            password=password,
            db=db
        )
        logging.info("connection bana liya",mydb)
        df=pd.read_sql("SELECT * FROM students",mydb)
        print(df.head())
        
    except Exception as ex:
        raise CustomException(ex, sys)

    