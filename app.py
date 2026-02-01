from ML_PROJECT.logger import logging
from ML_PROJECT.exception import CustomException
import sys

from ML_PROJECT.components.data_ingestion import DataIngestion
from ML_PROJECT.components.data_transformation import DataTransformation
from ML_PROJECT.components.model_tranier import ModelTrainer


if __name__ == "__main__":
    logging.info("Starting the ML Project Application")

    try:
        # Data Ingestion
        data_ingestion = DataIngestion()
        data_ingestion.initiate_data_ingestion()

        # Data Transformation
        data_transformation = DataTransformation()
        train_arr, test_arr, _ = data_transformation.initiate_data_transformation(
            train_path="artifacts/train.csv",
            test_path="artifacts/test.csv"
        )

        # Model Training
        model_trainer = ModelTrainer()
        print(
            model_trainer.initiate_model_trainer(
                train_array=train_arr,
                test_array=test_arr
            )
        )

    except Exception as e:
        logging.info("An exception occurred")
        raise CustomException("An error occurred in the main application", sys)
