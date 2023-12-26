import os
import shutil
from pathlib import Path

from setuptools import find_packages, setup

version = "0.2"
name = "UniConvert"

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name=name,
    version=version,
    packages=find_packages(),
    install_requires=[
        "certifi==2023.11.17",
        "charset-normalizer==3.3.2",
        "colorama==0.4.6",
        "decorator==4.4.2",
        "docutils==0.20.1",
        "idna==3.6",
        "imageio==2.33.1",
        "imageio-ffmpeg==0.4.9",
        "importlib-metadata==7.0.1",
        "jaraco.classes==3.3.0",
        "keyring==24.3.0",
        "markdown-it-py==3.0.0",
        "mdurl==0.1.2",
        "more-itertools==10.1.0",
        "moviepy==1.0.3",
        "nh3==0.2.15",
        "numpy==1.26.2",
        "Pillow==10.1.0",
        "pkginfo==1.9.6",
        "proglog==0.1.10",
        "Pygments==2.17.2",
        "python-dotenv==1.0.0",
        "pywin32-ctypes==0.2.2",
        "readme-renderer==42.0",
        "requests==2.31.0",
        "requests-toolbelt==1.0.0",
        "rfc3986==2.0.0",
        "rich==13.7.0",
        "tqdm==4.66.1",
        "twine==4.0.2",
        "types-Pillow==10.1.0.2",
        "urllib3==2.1.0",
        "zipp==3.17.0",
    ],
    long_description=long_description,
    long_description_content_type="text/markdown",
)


def move_dist(version: str) -> None:
    """Move files in dist to the correct version folder.

    Args:
        version (str): The version number.
    """
    dist_path = Path("dist")
    version_path = dist_path / version

    # Cria o diretório da versão se ainda não existir
    version_path.mkdir(parents=True, exist_ok=True)

    for file_name in os.listdir(dist_path):
        file_path = dist_path / file_name

        # Verifica se é um arquivo (não é um diretório)
        if file_path.is_file():
            # Move o arquivo para o diretório da versão
            shutil.move(file_path, version_path / file_name)


move_dist(version)
