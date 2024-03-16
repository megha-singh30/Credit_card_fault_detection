from setuptools import find_packages, setup
from typing import List

HYPHEN_DOT_E = '-e .'

# function to read requirements.txt file contents one by one
def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
    
    if HYPHEN_DOT_E in requirements:
        requirements.remove(HYPHEN_DOT_E)
        
    return requirements

# Setting up the details of the package to be installed for this particular project
# will also install the required libraries for this project using requirements.txt
setup(
    name = "Credit Card Fault Detection",
    version= '0.0.1',
    author= "Megha Singh",
    author_email="megha0330@gmail.com",
    install_requires = get_requirements('requirements.txt'),
    packages = find_packages()
)