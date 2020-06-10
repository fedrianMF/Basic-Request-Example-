"""Logger methods"""
import logging.config

# Loads the configuration file with all the necesary parameters
logging.config.fileConfig('logging.conf')

# Creates a LOGGER object to use in other clasess
LOGGER = logging.getLogger("trello_logger")
LOG_LEVEL = "DEBUG"
LOG_LEVELS = {
    "ERROR": logging.ERROR,
    "DEBUG": logging.DEBUG,
    "INFO": logging.INFO
}
LOGGER.setLevel(LOG_LEVELS.get(LOG_LEVEL))