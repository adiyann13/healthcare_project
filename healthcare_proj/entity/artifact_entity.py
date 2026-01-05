import os
from dataclasses import dataclass

@dataclass
class DataIngestionArtifacts:
    training_file_path:str
    testing_file_path:str

@dataclass
class DataValidationArtifacts:
    validation_status:bool
    valid_train_data_path:str
    valid_test_data_path:str
    invalid_train_data_path:str
    invalid_test_data_path:str
    drift_report_file_path:str

