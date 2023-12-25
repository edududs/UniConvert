from setuptools import setup, find_packages

setup(
    name="conversores_dudu",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "Pillow>=10.1.0",
        "types-Pillow>=10.1.0.2",
    ],
)
