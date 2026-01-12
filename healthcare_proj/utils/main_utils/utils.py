from healthcare_proj.exceptions.exception import CustomException
from healthcare_proj.logging.logger import logging
import os 
import yaml
import json
import sys
import numpy as np
import pickle
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score, precision_score, f1_score
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
            np.save(fl, arr)
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

def load_np_arrray(file_path:str)->np.array:
    try:
        with open(file_path ,"rb") as npfl:
            return np.load(npfl)
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

def evaluate_models(X_train, Y_train, X_test,Y_test,models,params):
    try:
        report:dict={}
        fittted_models = {}

        for i in range(len(list(models))):
            model = list(models.values())[i]
            model_name = list(models.keys())[i]
            parameters = params[model_name]

            gs = GridSearchCV(estimator=model, param_grid=parameters,cv=3)

            gs.fit(X_train,Y_train)

            model.set_params(**gs.best_params_)
            model.fit(X_train,Y_train)
            fittted_models[model_name]=model

            y_train_pred = model.predict(X_train)
            y_test_pred = model.predict(X_test)

            train_model_scores = accuracy_score(Y_train,y_train_pred)
            test_model_scores = accuracy_score(Y_test,y_test_pred)

            report[model_name] = test_model_scores
        
        return report, fittted_models

    except Exception as e:
         raise CustomException(e,sys)




