import os
import sys
import pandas as pd
import pymysql
from dotenv import load_dotenv
import numpy as np
import pickle
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import r2_score


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
    
def evaluate_models(X_train, y_train, X_test, y_test, models, params):
    try:
        report = {}

        for i in range(len(models)):
            model = list(models.values())[i]
            param = params[list(models.keys())[i]]

            gs = GridSearchCV(model, param, cv=5)
            gs.fit(X_train, y_train)

            model.set_params(**gs.best_params_)
            model.fit(X_train, y_train)

            y_test_pred = model.predict(X_test)

            test_model_score = r2_score(y_test, y_test_pred)

            report[list(models.keys())[i]] = test_model_score

        return report

    except Exception as e:
        raise CustomException(e, sys)
