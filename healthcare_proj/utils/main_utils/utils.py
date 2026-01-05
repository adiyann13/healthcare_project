from healthcare_proj.exceptions.exception import CustomException
from healthcare_proj.logging.logger import logging
import os 
import yaml
import json
import sys

def read_yaml(file_path:str):
    try:
        with open(file_path, 'rb') as ymf:
            return yaml.safe_load(ymf)
    except Exception as e:
        raise CustomException(e,sys)

def write_yaml(file_path:str, content:object, replace:bool =False)->None:
    try:
        if replace:
            if os.path.exists(file_path):
                os.remove(file_path)
        os.makedirs(os.path.dirname(file_path),exist_ok=True)
        with open(file_path, 'wb') as ylf:
            yaml.dump_all(content, ylf)
    except Exception as e:
        raise CustomException(e,sys)