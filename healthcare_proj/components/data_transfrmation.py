from healthcare_proj.entity.config_entity import DataTransformationConfig
from healthcare_proj.entity.artifact_entity import DataValidationArtifacts, DataTransformationArtifact
from healthcare_proj.exceptions.exception import CustomException
from healthcare_proj.logging.logger import logging
from healthcare_proj.constants.training_pipeline import TARGET_COL,DATA_TRANSFORMATION_IMPUTER_PARAMS
import os
import sys
from sklearn.model_selection import train_test_split
from sklearn.impute import KNNImputer
import pandas as pd
import numpy as np
from sklearn.pipeline import Pipeline
from healthcare_proj.utils.main_utils.utils import save_object,sve_array

class DataTransfromation:
    def __init__(self, data_validation_artifacts:DataValidationArtifacts , data_transformation_config:DataTransformationConfig):
        self.data_validation_artifacts = data_validation_artifacts
        self.data_transformation_config = data_transformation_config

    @staticmethod
    def read_csv(file_pth:str):
        try:
            data = pd.read_csv(file_pth)
            return data
        except Exception as e:
            raise CustomException(e,sys)
    
    def imputing(cls)->Pipeline:
        try:
            knn_imptr:KNNImputer = KNNImputer(**DATA_TRANSFORMATION_IMPUTER_PARAMS)
            processr:Pipeline = Pipeline([("imputer",knn_imptr)])
            return processr
        except Exception as e:
            raise CustomException(e,sys)
    
    def initiate_data_transformation(self):
        try:
            train_df = DataTransfromation.read_csv(self.data_validation_artifacts.valid_train_data_path)
            test_df = DataTransfromation.read_csv(self.data_validation_artifacts.valid_test_data_path)
            indep_features_train =train_df.drop([TARGET_COL], axis=1)
            dep_ftrs_train = train_df[TARGET_COL]
            indep_features_test = test_df.drop([TARGET_COL],axis=1)
            dep_ftrs_test = test_df[TARGET_COL]

            preprocess_obj_imp = self.imputing()
            knn_preprocessor = preprocess_obj_imp.fit(indep_features_train)
            preproceesed_train_df = knn_preprocessor.transform(indep_features_train)
            preprocessed_test_df = knn_preprocessor.transform(indep_features_test)

            train_arr = np.c_[preproceesed_train_df,np.array(dep_ftrs_train)]
            test_arr = np.c_[preprocessed_test_df,np.array(dep_ftrs_test)]

            sve_array(self.data_transformation_config.data_transformed_train_file_path , arr=train_arr)
            sve_array(self.data_transformation_config.data_transformed_test_file_path,arr=test_arr)
            save_object(self.data_transformation_config.transformed_file_obj_path,obj =knn_preprocessor )

            data_transformation_artifacts = DataTransformationArtifact(transformed_obj_file_path=self.data_transformation_config.transformed_file_obj_path,
                                                                        transformed_train_file_path=self.data_transformation_config.data_transformed_train_file_path,
                                                                        transformed_test_file_path=self.data_transformation_config.data_transformed_test_file_path)
            
            return data_transformation_artifacts
        except Exception as e:
            raise CustomException(e,sys)
        



        
        
