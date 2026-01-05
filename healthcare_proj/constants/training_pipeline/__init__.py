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


