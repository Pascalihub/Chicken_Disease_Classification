from chickenclassifier.pipeline.st_01_data_ingestion_pipeline import DataIngestionTrainingPipeline
from chickenclassifier.pipeline.st_02_preparebasemodel_pipeline import PrepareBaseModelTrainingPipeline
from chickenclassifier.pipeline.st_03_train_pipeline import ModelTrainingPipeline
from chickenclassifier.pipeline.st_04_evaluation_pipeline import EvaluationPipeline
from chickenclassifier.logger import logging




STAGE_NAME = "Data Ingestion Stage"

try:
    logging.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logging.info(
        f">>>>> stage {STAGE_NAME} completed <<<<< \n\nx===============x")
except Exception as e:
    logging.exception(e)
    raise e


STAGE_NAME = "Prepare Base Model"

try:
    logging.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    prepare_base_model = PrepareBaseModelTrainingPipeline()
    prepare_base_model.main()
    logging.info(
        f">>>>> stage {STAGE_NAME} completed <<<<< \n\nx===============x")
except Exception as e:
    logging.exception(e)
    raise e


STAGE_NAME = "Training"
try:
    logging.info(f"*******************")
    logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    model_trainer = ModelTrainingPipeline()
    model_trainer.main()
    logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logging.exception(e)
    raise e

STAGE_NAME = "Evaluation stage"
try:
    logging.info(f"*******************")
    logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    model_evalution = EvaluationPipeline()
    model_evalution.main()
    logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")

except Exception as e:
    logging.exception(e)
    raise e
