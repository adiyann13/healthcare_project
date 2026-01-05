from setuptools import find_packages,setup
from typing import List
from healthcare_proj.exceptions.exception import CustomException
import sys

hyphen_e = '-e .'
def get_requirements()->List[str]:
    
    requiremnts_lst:List[str] = []
    try:
        with open('requirements.txt', 'r') as fl:
            lines = fl.readlines()
            for lns in lines:
                rqrs = lns.replace('/n','')
                if rqrs != hyphen_e:
                    requiremnts_lst.append(rqrs)
    
    except Exception as e:
        raise CustomException(e,sys)

print(get_requirements())

setup(
    name = 'healthcare',
    version = '0.0.1',
    author = 'adiyan',
    packages=find_packages(),
    install_requires = get_requirements(),
)
