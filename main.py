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
from healthcare_proj.components.data_transfrmation import DataTransfromation
from healthcare_proj.entity.artifact_entity import DataTransformationArtifact
from healthcare_proj.entity.config_entity import DataTransformationConfig

from healthcare_proj.components.model_trainer import ModelTrainer
from healthcare_proj.entity.artifact_entity import ModelTrainerArtifact
from healthcare_proj.entity.config_entity import ModelTrainerConfig
import pymongo

if __name__ == "__main__":
    trainingpipeline = TrainingPipelineConfig()
    dataingestionconfig = DataIngestionConfig(training_pipeline_config=trainingpipeline)
    dataingestion = DataIngestion(dataingestionconfig)
    dataingestionconfigartifact = dataingestion.initiate_Data_ingestion()
    print(dataingestionconfigartifact)    
    logging.info("data ingestion completed")


    datavalidationconfig = DataValidationConfig(training_pipeline_config=trainingpipeline)
    datavalidation = DataValidation(dataingestionconfigartifact,datavalidationconfig )
    datavalidatyionartifacts = datavalidation.initiate_data_validation()
    print(dataingestionconfigartifact)

    datatransformconfig = DataTransformationConfig(training_pipeline_config=trainingpipeline)
    datatransform = DataTransfromation(data_validation_artifacts=datavalidatyionartifacts , data_transformation_config=datatransformconfig)
    datatransformedadrtifacts = datatransform.initiate_data_transformation()
    print(datatransformedadrtifacts)

    model_trainerconfig = ModelTrainerConfig(training_pipeline_config=trainingpipeline)
    model_trainer = ModelTrainer(datatransformedadrtifacts , model_trainer_config=model_trainerconfig)
    model_trainer_artifact = model_trainer.initiater_model_training()
    print(model_trainer_artifact)