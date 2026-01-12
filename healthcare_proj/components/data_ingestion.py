import os 
import sys
import numpy as np
import pandas as pd
from healthcare_proj.constants import training_pipeline
from healthcare_proj.entity.artifact_entity import DataIngestionArtifacts
from healthcare_proj.entity.config_entity import DataIngestionConfig
from healthcare_proj.exceptions.exception import CustomException
from healthcare_proj.logging import logger
from sklearn.model_selection import train_test_split
import certifi
from dotenv import load_dotenv

import pymongo

load_dotenv()

MONGO_DB_URL = os.getenv('MONGO_DB_URI')

class DataIngestion:
    def __init__(self, data_ingestion_config:DataIngestionConfig):
        try:
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            raise CustomException(e,sys)
    
    def export_data_from_mongo(self):
        try:
            db_name = self.data_ingestion_config.database_name
            collection_name = self.data_ingestion_config.collection_name
            self.mongo_client = pymongo.MongoClient(MONGO_DB_URL)
            collection = self.mongo_client[db_name][collection_name]


            data = pd.DataFrame(list(collection.find()))

            for dt in data:
                if dt == '_id':
                    data.drop(['_id'], axis=1, inplace=True)
            data.replace('nan' , np.nan , inplace=True)
            return data
        except Exception as e:
            raise CustomException(e,sys)
    

    def store_raw_data(self, df:pd.DataFrame):
        try:
            feature_store_path = self.data_ingestion_config.feature_store_file_path
            dir_path = os.path.dirname(feature_store_path)
            os.makedirs(dir_path,exist_ok=True)
            df.to_csv(feature_store_path , index=False,header=True)
            return df
        except Exception as e:
            raise CustomException(e,sys)
    
    def train_test_splitting(self,df:pd.DataFrame):
        try:
            training, testing = train_test_split(df , test_size=self.data_ingestion_config.train_test_split_ratio)
            dir_path = os.path.dirname(self.data_ingestion_config.training_file_path)
            os.makedirs(dir_path,exist_ok=True)
            training.to_csv(self.data_ingestion_config.training_file_path, index=False, header=True)
            testing.to_csv(self.data_ingestion_config.testing_file_path, index=False, header=True)
        
        except Exception as e:
            raise CustomException(e,sys)
    

    def initiate_Data_ingestion(self):
        try:
            dataframe = self.export_data_from_mongo()
            dataframe = self.store_raw_data(dataframe)
            self.train_test_splitting(dataframe)
            dataingestionartifacts = DataIngestionArtifacts(training_file_path=self.data_ingestion_config.training_file_path,
                                                            testing_file_path=self.data_ingestion_config.testing_file_path)
            return dataingestionartifacts
        except Exception as e:
            raise CustomException(e,sys)



