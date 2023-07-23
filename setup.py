from setuptools import find_packages,setup
from typing import List
def get_requirements()->List[str]:
    """
    This function will return a list of requirements
    """
    requirement_list:list[str] = []
    return requirement_list


setup(
    name = "Sensor_Fault_Detection",
    version="0.0.1",
    author="Kartikay_Garg",
    author_email="kartikaygarg282@gmail.com",
    packages = find_packages(),
    install_requires = get_requirements()
)