import os
from dataclasses import dataclass
from sklearn.metrics import f1_score,precision_score,accuracy_score

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

@dataclass
class DataTransformationArtifact:
    transformed_obj_file_path:str
    transformed_train_file_path:str
    transformed_test_file_path:str

@dataclass
class ModelMetrics:
    fl_scores:float
    precision_scores:float
    accuracy_score:float


@dataclass
class ModelTrainerArtifact:
    trained_model_artifact:str 
    trained_model_metrics:ModelMetrics
    testing_model_metrics:ModelMetrics
