import os
import sys
import json 
import certifi
import pymongo
import pandas as pd
import numpy as np
from healthcare_proj.exceptions.exception import CustomException
from healthcare_proj.logging.logger import logging
from dotenv import load_dotenv

load_dotenv()
MONOG_DB_URL = os.getenv('MONGO_DB_URI')


ca = certifi.where()

class HealdthDataExtract():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise CustomException(e,sys)
    
    def csv_to_json(self,file_path):
        try:
            data =pd.read_csv(file_path)
            data.reset_index(drop=True,inplace=True)
            records  = list(json.loads(data.T.to_json()).values())
            return records
        except Exception as e:
            raise CustomException(e,sys)
        
    def insert_data_to_mongo(self,records,database,collection):
        try:
            self.database = database
            self.collection = collection
            self.records = records
            self.mongo_client = pymongo.MongoClient(MONOG_DB_URL)
            self.database = self.mongo_client[self.database]
            self.collection = self.database[self.collection]
            self.collection.insert_many(self.records)
            return len(self.records)
        except Exception as e:
            raise CustomException(e,sys)


if __name__ == "__main__":
    file_path = 'dataset\diabetes.csv'
    database = 'healthcare2025'
    collection = 'healthcare'
    healthcareobj = HealdthDataExtract()
    converterd_data = healthcareobj.csv_to_json(file_path=file_path)
    print(converterd_data)
    inserted_records = healthcareobj.insert_data_to_mongo(converterd_data,database=database,collection=collection)
    print(inserted_records)
        


    
