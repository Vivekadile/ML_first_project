import logging
import os
from datetime import datetime

LOG_FILE=f"logs/log_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
log_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(os.path.dirname(log_path), exist_ok=True)


LOG_FILE=os.path.join("logs",LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE,
    format="[%(asctime)s] %(levelname)s - %(message)s",
    level=logging.INFO,

)
