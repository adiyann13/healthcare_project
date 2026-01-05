import os
import sys
from datetime import datetime
from healthcare_proj.constants import training_pipeline

class TrainingPipelineConfig:
    def __init__(self, timestamp:datetime =None):
        if timestamp is None:
            timestamp = datetime.now()
        
        timestamp_str = timestamp.strftime("%Y%m%H%d%M%S")

        self.pipeline_name = training_pipeline.PIPELINE_NAME
        self.artifact_name = training_pipeline.ARTIFFACT_DIR
        self.artifact_dir = os.path.join(self.artifact_name,timestamp_str)
        self.model_dir = os.path.join('final_model')
        self.timestamp:str = timestamp


class DataIngestionConfig:
    def __init__(self, training_pipeline_config:TrainingPipelineConfig):
        self.data_ingestion_dir:str = os.path.join(training_pipeline_config.artifact_dir, training_pipeline.DATA_INGETION_DIR_NAME)
    
        self.feature_store_file_path:str = os.path.join(self.data_ingestion_dir, training_pipeline.DATA_INGESTION_FEATURE_STORE,training_pipeline.FILE_NAME)

        self.training_file_path:str = os.path.join(self.data_ingestion_dir, training_pipeline.DATA_INGESTION_INGESTED_DATA,training_pipeline.TRAIN_FILE_NAME)

        self.testing_file_path:str = os.path.join(self.data_ingestion_dir,training_pipeline.DATA_INGESTION_INGESTED_DATA, training_pipeline.TEST_FILE_NAME)

        self.train_test_split_ratio = training_pipeline.DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO
        self.database_name = training_pipeline.DATA_INGESTION_DATABASE_NAME
        self.collection_name = training_pipeline.DATA_INGETSION_COLLECTION_NAME


class DataValidationConfig:
    def __init__(self,training_pipeline_config:TrainingPipelineConfig):
        self.data_validation_dir:str = os.path.join(training_pipeline_config.artifact_dir, training_pipeline.DATA_VALIDATION_DIR_NAME)
        self.valid_data:str = os.path.join(self.data_validation_dir , training_pipeline.DATA_VALIDATION_VALID_DIR)
        self.invalid_data:str =os.path.join(self.data_validation_dir,training_pipeline.DATA_VALIDATION_INVALID_DIR)
        self.valid_train_data_path:str=os.path.join(self.data_validation_dir,training_pipeline.TRAIN_FILE_NAME)
        self.invalid_train_data_path:str = os.path.join(self.data_validation_dir , training_pipeline.TRAIN_FILE_NAME)
        self.valid_test_data_path:str = os.path.join(self.data_validation_dir,training_pipeline.TEST_FILE_NAME)
        self.invalid_test_data_path:str = os.path.join(self.data_validation_dir, training_pipeline.TEST_FILE_NAME)
        self.data_drift_report:str = os.path.join(
            self.data_validation_dir,
            training_pipeline.DATA_VALIDATION_DRIFT_REPORT,
            training_pipeline.DATA_VALIDATION_FINAL_REPORT
        )
