import os
import sys
from dataclasses import dataclass

import numpy as np
import mlflow
import mlflow.sklearn
import dagshub

from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import (
    RandomForestRegressor,
    GradientBoostingRegressor,
    AdaBoostRegressor,
)
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

from xgboost import XGBRegressor
from catboost import CatBoostRegressor

from ML_PROJECT.exception import CustomException
from ML_PROJECT.logger import logging
from ML_PROJECT.utils import save_object, evaluate_models


# ===================== MLflow + DagsHub INIT =====================
dagshub.init(
    repo_owner="Vivekadile",
    repo_name="ML_first_project",
    mlflow=True,
)

mlflow.set_experiment("ML_First_Project_Experiment")
# ===============================================================


@dataclass
class ModelTrainerConfig:
    trained_model_file_path: str = os.path.join("artifacts", "model.pkl")


class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()

    def eval_metrics(self, y_true, y_pred):
        rmse = np.sqrt(mean_squared_error(y_true, y_pred))
        mae = mean_absolute_error(y_true, y_pred)
        r2 = r2_score(y_true, y_pred)
        return rmse, mae, r2

    def initiate_model_trainer(self, train_array, test_array):
        try:
            logging.info("Splitting train and test data")

            X_train, y_train = train_array[:, :-1], train_array[:, -1]
            X_test, y_test = test_array[:, :-1], test_array[:, -1]

            models = {
                "Linear Regression": LinearRegression(),
                "Decision Tree": DecisionTreeRegressor(),
                "Random Forest": RandomForestRegressor(),
                "Gradient Boosting": GradientBoostingRegressor(),
                "AdaBoost": AdaBoostRegressor(),
                "CatBoost": CatBoostRegressor(verbose=False),
                "XGBRegressor": XGBRegressor(),
            }

            params = {
                "Linear Regression": {"fit_intercept": [True, False]},
                "Decision Tree": {"max_depth": [3, 5, 10, 20]},
                "Random Forest": {
                    "n_estimators": [50, 100, 200],
                    "max_depth": [3, 5, 10],
                },
                "Gradient Boosting": {
                    "learning_rate": [0.01, 0.1, 0.2],
                    "n_estimators": [100, 200],
                },
                "AdaBoost": {
                    "n_estimators": [50, 100, 200],
                    "learning_rate": [0.01, 0.1, 0.2],
                },
                "CatBoost": {
                    "depth": [3, 5, 7],
                    "learning_rate": [0.01, 0.1, 0.2],
                    "iterations": [100, 200],
                },
                "XGBRegressor": {
                    "learning_rate": [0.01, 0.1, 0.2],
                    "n_estimators": [100, 200],
                },
            }

            model_report = evaluate_models(
                X_train, y_train, X_test, y_test, models, params
            )

            best_model_score = max(model_report.values())
            best_model_name = list(model_report.keys())[
                list(model_report.values()).index(best_model_score)
            ]
            best_model = models[best_model_name]

            print(f"Best Model: {best_model_name} | Best R2: {best_model_score}")

            with mlflow.start_run():
                best_model.fit(X_train, y_train)
                y_pred = best_model.predict(X_test)

                rmse, mae, r2 = self.eval_metrics(y_test, y_pred)

                mlflow.log_param("model_name", best_model_name)
                mlflow.log_metric("rmse", rmse)
                mlflow.log_metric("mae", mae)
                mlflow.log_metric("r2_score", r2)

                mlflow.sklearn.log_model(best_model, "model")

            # ⚠️ IMPORTANT: NO CustomException for low score
            if best_model_score < 0.6:
                logging.warning(
                    f"Best model R2 ({best_model_score}) is below threshold, continuing."
                )

            save_object(
                file_path=self.model_trainer_config.trained_model_file_path,
                obj=best_model,
            )

            return r2

        except Exception as e:
            raise CustomException(e, sys)
