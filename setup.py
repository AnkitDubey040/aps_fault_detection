from setuptools import find_packages,setup
from typing import List

REQUIREMENT_FILE_NAME = "requirements.txt"
# NOw to trigger reuirements.txt file wqe use this : 
HYPHEN_E_DOT = "-e."



# function that contains libraries to be used in this project are called by get_requirement func (libraries in requirements.txt)
# Now since I want to read each library as form of a list so i will convert it as a list 
def get_requirements()->List[str]:
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        requirenemt_list = requirement_file.readlines()
        # since we are reading each line so automaticall in list \n will also come so we ned to remove it : 
    requirenemt_list = [requirement_name.replace("\n" , "") for requirement_name in requirement_list]

    # Since we don't require -e. in our lisst so we remove it: 
    if HYPHEN_E_DOT in requirement_list:
        requirement_list.remove(HYPHEN_E_DOT)
    return requirement_list


setup(
    name = "sensor",
    version = "0.0.2",
    author = "AnkitDubey040",
    author_email="ankitdubey04052001@gmail.com",
    packages = find_packages(), 
    install_requirements = get_requirements()
    # sensor folder will have all the source code 
    # what find packages does is go to sensor folder and find all the packages used
    # also we create a file __init__.py file in sensor because any folder with this file is considered as a package by find_packages()
)