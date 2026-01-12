import os
import sys
import pandas as pd
import numpy as np

TARGET_COL = 'Outcome'
PIPELINE_NAME:str = 'Diabetes_data'
ARTIFFACT_DIR:str = 'Artifacts'
FILE_NAME:str = 'diabetes.csv'

TRAIN_FILE_NAME = 'train.csv'
TEST_FILE_NAME = 'test.csv'

SAVED_MODEL_DEIR:str = os.path.join('saved_models')
MODEL_FILE_NAME = 'model.pkl'


##data ingestion constants

DATA_INGETSION_COLLECTION_NAME:str = 'healthcare'
DATA_INGESTION_DATABASE_NAME:str = 'healthcare2025'
DATA_INGETION_DIR_NAME:str = 'data_ingestion_dir'
DATA_INGESTION_FEATURE_STORE:str = 'data_ingestion_feature_store'
DATA_INGESTION_INGESTED_DATA:str = 'ingested'
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO:float = 0.2

##data validation constants

DATA_SCHEMA_FILE_PATH:str = os.path.join('data_schema' , 'schema.yaml')

DATA_VALIDATION_DIR_NAME:str = 'data_validation'
DATA_VALIDATION_VALID_DIR:str  = 'validated_data'
DATA_VALIDATION_INVALID_DIR:str = 'invaled_data'
DATA_VALIDATION_DRIFT_REPORT:str = 'data_drift'
DATA_VALIDATION_FINAL_REPORT:str = 'report.yaml'


PRE_PROCESSING_FILE_PATH = 'preprocessed.pkl'

DATA_TRANSFORMATION_DIR_NAME = 'Dta_transformation'
DATA_TRANSFORMATION_TRANSFORMED_DATA:str = 'transformed_data'
DATA_TRANSFORMATION_TRANSFORMED_OBJECT:str = 'transformed_obj'

DATA_TRANSFORMATION_IMPUTER_PARAMS:dict ={
    "missing_values": np.nan,
    'n_neighbors':3 , 
    'weights':'uniform',
}


MODEL_TRAINER_DIR_NAME:str = "model_trainer"
TRAINED_MODEL_NAME :str = "model.pkl"
TRAINING_DATA_TRAINED_MODEL:str = 'trained_model'
MODEL_EXPECTED_SCORE:float = 0.65
