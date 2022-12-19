from setuptools import find_packages,setup

# function that contains libraries to be used in this project : (libraries in requirements.txt)
def get_requirements():
    pass


setup(
    name = "sensor",
    version = "0.0.1",
    author = "ankitdubey04052001@gmail.com",
    packages = find_packages(), 
    install_requirements = get_requirements()
    # sensor folder will have all the source code 
    # what find packages does is go to sensor folder and find all the packages used
    # also we create a file __init__.py file in sensor because any folder with this file is considered as a package by find_packages()
)