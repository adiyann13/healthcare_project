from healthcare_proj.entity.artifact_entity import ModelMetrics
from healthcare_proj.exceptions.exception import CustomException
from sklearn.metrics import f1_score, accuracy_score, precision_score
import sys

def get_classification_scores(y_actual, y_pred)->ModelMetrics:
    try:
        model_f1_score= f1_score(y_actual, y_pred)
        mode_accuracy = accuracy_score(y_actual,y_pred)
        model_precision = precision_score(y_actual ,y_pred)

        metrics  = ModelMetrics(fl_scores=model_f1_score , precision_scores=model_precision,accuracy_score=mode_accuracy)
        return metrics
    except Exception as e:
        raise CustomException(e,sys)