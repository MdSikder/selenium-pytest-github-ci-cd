import logging


def setup_logger():
    logger = logging.getLogger('AutomationLogger')
    logger.setLevel(logging.INFO)
    handler = logging.FileHandler('logs/test_log.log')
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger


logger = setup_logger()
