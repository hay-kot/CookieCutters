import logging
from pathlib import Path

import coloredlogs

LOGGER_LEVEL = "INFO"
CWD = Path(__file__).parent
LOGGER_FILE = CWD.joinpath("resources", "RACBuddy.log")


logging.basicConfig(
    level=LOGGER_LEVEL,
    format="%(asctime)s %(levelname)s: %(message)s",
    datefmt="%d-%b-%y %H:%M:%S", 
    filename=LOGGER_FILE,
)
coloredlogs.install(
    level=LOGGER_LEVEL,
    fmt="%(asctime)s %(levelname)s: %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
)

logger = logging.getLogger(__name__)


""" Logging Cheat Sheet
logger.debug("this is a debugging message")
logger.info("this is an informational message")
logger.warning("this is a warning message")
logger.error("this is an error message")
logger.critical("this is a critical message")
"""

if __name__ == "__main__":
    logger.debug("this is a debugging message")
    logger.info("this is an informational message")
    logger.warning("this is a warning message")
    logger.error("this is an error message")
    logger.critical("this is a critical message")
