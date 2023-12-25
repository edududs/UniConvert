from setuptools import setup, find_packages
from dotenv import load_dotenv
load_dotenv()

setup(
    name="conversores_dudu",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "Pillow>=10.1.0",
        "types-Pillow>=10.1.0.2",
    ],
)
