import os 
from pathlib import Path 
import logging

logging.basicConfig(level=logging.INFO)


project_name="ML_PROJECT"
list_of_file=[
    f"src/{project_name}/_init_•py",
    f"src/{project_name}/components/_init_•py",
    f"src/{project_name}/components/data_ingestion.py",
    f"src/{project_name}/components/data_transformation.py", 
    f"src/{project_name}/components/model_tranier.py",
    f"src/{project_name}/components/model_monitering-py", 
    f"src/{project_name}/pipelines/_init_•py",
    f"src/{project_name}/pipelines/training_pipeline.py",
    f"src/{project_name}/pipelines/prediction_pipeline.py",
    f"src/{project_name}/exception.py",
    f"src/{project_name}/logger.py",
    f"src/{project_name}/utils.py",
    "app.py",
    "main.py",
    "dockerfile",
    "requirements.txt",
    "setup.py",
    
    
    

]

for filepath in list_of_file:
    filepath=Path(filepath)
    filedir,filename=os.path.split(filepath)
    if filedir !="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating directory:{filedir} for file :{filename}")
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open (filepath,"w") as fp:
            pass 


    else:
        logging.info(f"File :{filename} already exists at :{filedir}")