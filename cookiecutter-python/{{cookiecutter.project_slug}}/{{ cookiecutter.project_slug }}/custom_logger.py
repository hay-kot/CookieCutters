import logging

import coloredlogs

logging.basicConfig(level=logging.DEBUG, )
logging.basicConfig(format='%(asctime)s %(levelname)s: %(message)s', datefmt='%d-%b-%y %H:%M:%S')
coloredlogs.install(level='DEBUG', fmt='%(asctime)s %(levelname)s: %(message)s', datefmt='%d-%b-%y %H:%M:%S')

logger = logging.getLogger(__name__)

""" Logging Cheat Sheet
logger.debug("this is a debugging message")
logger.info("this is an informational message")
logger.warning("this is a warning message")
logger.error("this is an error message")
logger.critical("this is a critical message")
"""