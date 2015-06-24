__author__ = 'Aiden'

import ConfigParser, logging, os

# config.cfg.read(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'conf', 'config.cfg.cfg'))

DEFAULT_SECTION = 'Default'
LOG_NAME = 'test.log'

config = ConfigParser.ConfigParser()
config_file = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'conf', 'config.cfg')
config.read(config_file)

url = config.get(DEFAULT_SECTION, "url")


def getLogger(log_name, level):

    # setup a logger
    logger = logging.getLogger(log_name)
    logger.setLevel(level)

    # build a handler, write log to file
    fh = logging.FileHandler(LOG_NAME)
    fh.setLevel(logging.DEBUG)

    # build a handler, writer log to console
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    # define log format
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)

    # set handler in to logger
    logger.addHandler(fh)
    logger.addHandler(ch)

    # return logger
    return logger