import logging 
import os 
from datetime import datetime 
LOG_FILE_NAME = f"{datetime.now().strftime('%m%d%Y__%H%M%S')}.log"
LOG_FILE_DIR = os.path.join(os.getcwd(),"logs")  
logging.basicConfig(filename=LOG_FILE_PATH,format=  "[ %(asctime)s  ]%(lineno)d %(name)s - %(levelname)s - %(message)s" ,level=logging.INFO)
