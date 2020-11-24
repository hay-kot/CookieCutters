from local_pkgs.custom_logger import logger
from pathlib import Path

CWD = Path(__file__).parent
APP_VERSION = "{{ cookiecutter.version }}"
REPO_URL = "https://api.github.com/repos/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/releases/latest"

if __name__ == "__main__":
    logger.debug("this is a debugging message")
    logger.info("this is an informational message")
    logger.warning("this is a warning message")
    logger.error("this is an error message")
    logger.critical("this is a critical message")

