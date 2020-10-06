from custom_logger import logger

CWD = Path(__file__).parent
APP_VERSION = "{{ cookiecutter.version }}"
REPO_URL = "https://api.github.com/repos/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/releases/latest"

if __name__ == "__main__":
    pass
