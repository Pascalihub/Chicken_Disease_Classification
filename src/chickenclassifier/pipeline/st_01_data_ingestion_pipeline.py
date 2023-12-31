# Create the pipeline
from chickenclassifier.config.configuration import ConfigurationManager
from chickenclassifier.components.data_ingestion import DataIngestion
from chickenclassifier.logger import logging


STAGE_NAME = "Data Ingestion Stage"


class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()


if __name__ == '__main__':
    try:
        logging.info(f">>>>> stage {STAGE_NAME} started <<<<<")
        data_ingestion = DataIngestionTrainingPipeline()
        data_ingestion.main()
        logging.info(
            f">>>>> stage {STAGE_NAME} completed <<<<< \n\nx===============x")
    except Exception as e:
        logging.exception(e)
        raise e
