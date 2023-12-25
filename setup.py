from setuptools import setup, find_packages

setup(
    name="conversores_dudu",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "moviepy>=1.0.3",
        "numpy>=1.26.2",
        "Pillow>=10.1.0",
        "twine>=4.0.2",
        "types-Pillow>=10.1.0.2",
    ],
)
