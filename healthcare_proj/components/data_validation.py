from healthcare_proj.constants import training_pipeline
from healthcare_proj.components.data_ingestion import DataIngestion,DataIngestionConfig
from healthcare_proj.entity.artifact_entity import DataValidationArtifacts,DataIngestionArtifacts
from healthcare_proj.entity.config_entity import DataValidationConfig
from healthcare_proj.exceptions.exception import CustomException
from healthcare_proj.logging.logger import logging
import os 
from dotenv import load_dotenv
from healthcare_proj.constants.training_pipeline import DATA_SCHEMA_FILE_PATH
from healthcare_proj.utils.main_utils.utils import read_yaml,write_yaml
load_dotenv()
import sys
import pandas as pd
import numpy as np
from scipy.stats import ks_2samp

class DataValidation:
    def __init__(self , data_ingestion_artifacts:DataIngestionArtifacts , data_validation_config:DataValidationConfig):
        try:
            self.data_ingestion_artifact = data_ingestion_artifacts
            self.data_validation_config = data_validation_config
            self.schema_read = read_yaml(DATA_SCHEMA_FILE_PATH)
        
        except Exception as e:
            raise CustomException(e,sys)
    
    @staticmethod
    def read_data(file_path:str) -> pd.DataFrame:
        return pd.read_csv(file_path)
    
    def validating_data(self,df:pd.DataFrame)->bool:
        try:
            no_of_cols = len(self.schema_read)
            df_cols = len(df.columns)
            if no_of_cols == df_cols :
                return True
            else:
                return False
        except Exception as e:
            raise CustomException(e,sys)
    
    def detect_data_drift(self,base_df,current_Df, threshold=0.05)->bool:
        try:
            status = True
            report={}
            for cols in base_df.columns:
                d1 = base_df[cols]
                d2 = current_Df[cols]
                sapmle_test = ks_2samp(d1,d2)
                if threshold <=sapmle_test.pvalue:
                    is_found = False
                else:
                    is_found=True
                    status =False
                report.update({'p_value':float(sapmle_test.pvalue), "drift_status":is_found})
                drift_report_file_path = self.data_validation_config.data_drift_report
                dir_path = os.path.dirname(drift_report_file_path)
                os.makedirs(dir_path , exist_ok=True)
                write_yaml(file_path=drift_report_file_path,content=report)
        except Exception as e:
            raise CustomException(e,sys)
    
    def initiate_data_validation(self):
        try:
            train_file_path= self.data_ingestion_artifact.training_file_path
            test_file_path = self.data_ingestion_artifact.testing_file_path

            training_df = DataValidation.read_data(train_file_path)
            testing_df =DataValidation.read_data(test_file_path)

            train_status = self.validating_data(training_df)
            if train_status ==True:
                return f'the train data  columns are same  '
            
            test_status = self.validating_data(testing_df)
            if test_status ==True:
                return f'the test data columns are same '
            
            drift_status = self.detect_data_drift(base_df=training_df,current_Df=testing_df)
            dir_pth =os.path.dirname(self.data_validation_config.valid_train_data_path)
            os.makedirs(dir_pth , exist_ok=True)
            training_df.to_csv(self.data_validation_config.valid_train_data_path, index=False,header=True)

            data_validation_artifact = DataValidationArtifacts(
                validation_status=drift_status,
                valid_train_data_path=self.data_ingestion_artifact.training_file_path,
                valid_test_data_path=self.data_ingestion_artifact.test_file_path,
                invalid_train_path = None,
                invalid_test_data = None,
                drift_report_file_path=self.data_validation_config.data_drift_report,
            )
            
            return data_validation_artifact
        
        except Exception as e:
            raise CustomException(e,sys)


                



