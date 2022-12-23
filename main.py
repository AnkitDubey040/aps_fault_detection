from sensor.pipeline.training_pipeline import start_training_pipeline
from sensor.pipeline.batch_prediction import start_batch_prediction
from sensor.logger import logging
from sensor.exception import SensorException
import sys,os



file_path = "/config/workspace/aps_failure_training_set1.csv"
print(__name__)
if __name__=="__main__":
    try:
      #start_training_pipeline() 
      output_file = start_batch_prediction(input_file_path=file_path)
      print(output_file)
    except Exception as e:
      raise SensorException(e,sys)

