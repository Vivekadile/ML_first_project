import os
import sys
import pandas as pd
import pymysql
from dotenv import load_dotenv

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
