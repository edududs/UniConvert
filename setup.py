from setuptools import setup, find_packages

with open("requirements.txt", "r") as f:
    requirements = f.read()

setup(
    name="conversores_dudu",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        requirements
    ],
)
