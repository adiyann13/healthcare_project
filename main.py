from healthcare_proj.components.data_ingestion import DataIngestion
from healthcare_proj.components.data_ingestion import DataIngestionArtifacts
from healthcare_proj.components.data_ingestion import DataIngestionConfig
from healthcare_proj.entity.artifact_entity import DataIngestionArtifacts
from healthcare_proj.entity.config_entity import DataIngestionConfig,TrainingPipelineConfig
from healthcare_proj.constants import training_pipeline
from healthcare_proj.entity.artifact_entity import DataValidationArtifacts
from healthcare_proj.entity.config_entity import DataValidationConfig
from healthcare_proj.components.data_validation import DataValidation
import os
from healthcare_proj.exceptions.exception import CustomException
from healthcare_proj.logging.logger import logging

if __name__ == "__main__":
    trainingpipeline = TrainingPipelineConfig()
    dataingestionconfig = DataIngestionConfig(training_pipeline_config=trainingpipeline)
    dataingestion = DataIngestion(dataingestionconfig)
    dataingestionconfigartifact = dataingestion.initiate_Data_ingestion()
    print(dataingestionconfigartifact)    
    logging.info("data ingestion completed")


    datavalidationconfig = DataValidationConfig(training_pipeline_config=training_pipeline)
    datavalidation = DataValidation(dataingestionconfigartifact,datavalidationconfig )
    datavalidatyionartifacts = datavalidation.initiate_data_validation()
    print(dataingestionconfigartifact)