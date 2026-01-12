from healthcare_proj.exceptions.exception import CustomException
from healthcare_proj.logging.logger import logging
import os 
import yaml
import json
import sys
import numpy as np
import pickle
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
        with open(file_path, 'w') as ylf:
            yaml.dump_all(content, ylf)
    except Exception as e:
        raise CustomException(e,sys)
    
def sve_array(file_pth:str , arr:np.array):
    try:
        dir_path = os.path.dirname(file_pth)
        os.makedirs(dir_path,exist_ok=True)
        with open(file_pth,'wb') as fl:
            np.save(fl,'array')
    except Exception as e:
        raise CustomException(e,sys)

def save_object(file_pth:str, obj:object):
    try:
        dir_pth = os.path.dirname(file_pth)
        os.makedirs(dir_pth, exist_ok=True)
        with open(file_pth, 'wb') as ob:
            pickle.dump(obj, ob)
    except Exception as e:
        raise CustomException(e,sys)

def load_object(file_path:str)->object:
    try:
        if not os.path.exists(file_path):
            raise Exception(f'file does not exists')
        else:
            with open(file_path,'rb') as ll:
                return pickle.load(ll)
    except Exception as e:
        raise CustomException(e,sys)





