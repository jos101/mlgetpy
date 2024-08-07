from setuptools import setup, find_packages


with open("README.md", "r") as file:
    long_description = file.read()

with open("requirements.txt", "r") as file:
    requirements = [r.strip() for r in file.readlines()]


setup(
    name="mlrgetpy",
    version="1.0.0",
    description="Python Package to extract data sets from the Center for Machine Learning and Intelligent Systems",
    long_description=long_description,
    #packages=["mlrgetpy"],
    packages=find_packages(),
    entry_points={"console_scripts": ["mlrgetpy=mlrgetpy.cli.repo:main"]},
    install_requires=requirements,
)
