from chickenclassifier.config.configuration import ConfigurationManager
from chickenclassifier.components.evaluation import Evaluation
from chickenclassifier.logger import logging

STAGE_NAME = "TEvaluation"


class EvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        val_config = config.get_validation_config()
        evaluation = Evaluation(val_config)
        evaluation.evaluation()
        evaluation.save_score()


if __name__ == '__main__':
    try:
        logging.info(f">>>>> stage {STAGE_NAME} started <<<<<")
        obj = EvaluationPipeline()
        obj.main()
        logging.info(
            f">>>>> stage {STAGE_NAME} completed <<<<< \n\nx===============x")
    except Exception as e:
        logging.exception(e)
        raise e
