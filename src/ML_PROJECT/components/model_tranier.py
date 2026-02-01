import os
import sys
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from dataclasses import dataclass
from catboost import CatBoostClassifier
from xgboost import XGBRegressor

from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, AdaBoostClassifier
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import r2_score
from ML_PROJECT.exception import CustomException
from ML_PROJECT.logger import logging
from ML_PROJECT.utils import save_object, evaluate_models

@dataclass
class ModelTrainerConfig:
    trained_model_file_path: str = os.path.join("artifacts", "model.pkl")

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()  
    def initiate_model_trainer(self, train_array, test_array):
        try:
            logging.info("split traina nd test data ")
            X_train, y_train, X_test, y_test = (
                train_array[:, :-1],
                train_array[:, -1],
                test_array[:, :-1],
                test_array[:, -1],
            )
            model = {
                "Random Forest": RandomForestClassifier(),
                "Decision Tree": DecisionTreeClassifier(),
                "Linear Regression": LinearRegression(),
                "Gradient Boosting": GradientBoostingClassifier(),
                "AdaBoost": AdaBoostClassifier(),
                "CatBoost": CatBoostClassifier(verbose=False),
                "XGBRegressor": XGBRegressor(),
            }
            parameters = {
                "Decision Tree": {
                    'criterion':['gini','entropy'],
                    'max_depth':[3,5,10,20],
                },  
                "Random Forest": {
                    'n_estimators':[50,100,200],
                    'max_depth':[3,5,10],
                },  
                "Linear Regression": {
                    'fit_intercept':[True,False],
                },
                "Gradient Boosting": {
                    'learning_rate':[0.01,0.1,0.2],
                    'n_estimators':[100,200],
                },
                LinearRegression: {
                    'fit_intercept':[True,False],
                },
                "XGBRegressor": {
                    'learning_rate':[0.01,0.1,0.2],
                    'n_estimators':[100,200],
                },
                "AdaBoost": {
                    'n_estimators':[50,100,200],
                    'learning_rate':[0.01,0.1,0.2],
                },
                "CatBoost": {
                    'depth':[3,5,7],
                    'learning_rate':[0.01,0.1,0.2],
                    'iterations':[100,200],
                }
            }

            model_report: dict = evaluate_models(X_train, y_train, X_test, y_test, model, parameters)

            best_model_score = max(sorted(model_report.values())) 
            best_model_name = list(model_report.keys())[
                list(model_report.values()).index(best_model_score)
            ]
            best_model = model[best_model_name]

            if best_model_score < 0.6:
                raise CustomException("No best model found")
            logging.info("Best model found on both training and testing dataset")
            save_object(
                file_path=self.model_trainer_config.trained_model_file_path,
                obj=best_model
            )
            predicted = best_model.predict(X_test)
            r2_square = r2_score(y_test, predicted)
            return r2_square
                    




        except Exception as e:
            raise CustomException(e, sys)
      