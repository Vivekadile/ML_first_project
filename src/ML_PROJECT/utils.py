import os
import sys
import pandas as pd
import pymysql
from dotenv import load_dotenv
import numpy as np
import pickle

from ML_PROJECT.exception import CustomException
from ML_PROJECT.logger import logging

load_dotenv()

host = os.getenv("host")
user = os.getenv("user")
password = os.getenv("password")
db = os.getenv("db")

def read_sql_data():
    logging.info("Reading data from MySQL database")
    try:
        mydb = pymysql.connect(
            host=host,
            user=user,
            password=password,
            db=db
        )

        logging.info("MySQL connection established")

        df = pd.read_sql("SELECT * FROM students", mydb)
        logging.info("Data read successfully from students table")

        return df   # ✅ THIS WAS MISSING

    except Exception as ex:
        raise CustomException(ex, sys)
    
def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, 'wb') as file_obj:
            pickle.dump(obj, file_obj)

        logging.info(f"Object saved successfully at {file_path}")

    except Exception as e:
        raise CustomException(e, sys)   
