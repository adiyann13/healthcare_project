from healthcare_proj.entity.config_entity import ModelTrainerConfig,DataTransformationConfig
from healthcare_proj.entity.artifact_entity import DataTransformationArtifact,ModelTrainerArtifact
from healthcare_proj.constants import training_pipeline
from healthcare_proj.exceptions.exception import CustomException
from healthcare_proj.logging import logger
from healthcare_proj.utils.main_utils.utils import load_object,save_object,sve_array, load_np_arrray
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import mlflow
import dagshub
import os
import sys
from healthcare_proj.utils.main_utils.utils import evaluate_models
from healthcare_proj.utils.ml_utils.metrics.classification_metrics import get_classification_scores

class ModelTrainer:
    def __init__(self , data_transformed_artifacts:DataTransformationArtifact, model_trainer_config:ModelTrainerConfig):
        try:
            self.data_transformed_artifacts=data_transformed_artifacts
            self.model_trainer_config=model_trainer_config
        except Exception as e:
             raise CustomException(e,sys)
    
    def training_model(self, x_train, y_train, x_test,y_test):
        try:
            models={
                'RandomForestModel': RandomForestClassifier(),
                'KNNModel':KNeighborsClassifier(),
                'DecisionTree':DecisionTreeClassifier(),
                'LogisticRegression':LogisticRegression()
            }
            
            params={
                'RandomForestModel':{
                    'n_estimators':[100,120,140],
                    'max_depth':[5,8,12,15]
                },
                'KNNModel':{
                },
                'DecisionTree':{
                    "criterion":['gini', 'entropy'],
                    'max_depth':[5,8,10,12,15],
                    'min_samples_split':[2,4,6,8]
                },
                'LogisticRegression':{
                    'penalty':['l1','l2', 'elasticnet'],
                }
            }

            model_report , fitted_models = evaluate_models(X_train= x_train,Y_train=y_train,X_test=x_test,Y_test=y_test,models=models, params=params)
            best_model_score = max(sorted(model_report.values()))

            best_model_name = list(model_report.keys())[
                list(model_report.values()).index(best_model_score)
            ]

            best_model = fitted_models[best_model_name]

            y_train_pred = best_model.predict(x_train)
            train_model_metrics = get_classification_scores(y_actual=y_train, y_pred=y_train_pred)

            y_test_pred = best_model.predict(x_test)
            test_model_metrics = get_classification_scores(y_actual=y_test , y_pred=y_test_pred)

            save_object(self.model_trainer_config.trained_model_file_path, best_model)

            model_trainer_artifacts = ModelTrainerArtifact(
                trained_model_artifact=self.model_trainer_config.trained_model_file_path,
                trained_model_metrics=train_model_metrics,
                testing_model_metrics=test_model_metrics
            )
            return model_trainer_artifacts
        except Exception as e:
            raise CustomException(e,sys)
    
    def initiater_model_training(self)-> ModelTrainerArtifact:
        try:
            train_file_path:str = self.data_transformed_artifacts.transformed_train_file_path
            test_file_path:str = self.data_transformed_artifacts.transformed_test_file_path

            train_arry = load_np_arrray(train_file_path)
            test_arry = load_np_arrray(test_file_path)

            x_train,y_train,x_test,y_test = (
                train_arry[:,:-1],
                train_arry[:,-1],
                test_arry[:,:-1],
                test_arry[:,-1],
            )
            modeltrainer_artifacts = self.training_model(x_train,y_train,x_test,y_test)
            return modeltrainer_artifacts
        except Exception as e:
            raise CustomException(e,sys)
    