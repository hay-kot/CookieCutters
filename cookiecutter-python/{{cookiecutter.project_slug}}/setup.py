from pathlib import Path

from setuptools import find_packages, setup

PKG_PATH = "./{{ cookiecutter.project_slug }}/{{ cookiecutter.project_slug }}/local_pkgs"

setup(
    name="local_pkgs",
    version="0.1.0",
    packages=find_packages(where=PKG_PATH),
    include_package_data=True,
    zip_safe=False,
)
