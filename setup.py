from setuptools import find_packages,setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    requirement = []
    with open(file_path) as file_obj:
        requirement = file_obj.readlines()
        requirement = [req.replace('\n','') for req in requirement]
    
    return requirement




setup(
    name='Fault Detection',
    version='0.0.1',
    author='Adarsh',
    author_email='adarshkeshrwani144@gmail.com',
    install_requires = get_requirements('requirements.txt'),
    packages=find_packages()
)