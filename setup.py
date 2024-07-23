from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT="-e ."

def get_requirements(file_path:str)->List[str]:
    """
    this funciton will return the list of requeirements
    """
    requeirements=[]
    with open(file_path) as file_obj:
        requeirements =file_obj.readlines()
        requeirements = [req.replace("\n","") for req in requeirements]
        
        if HYPEN_E_DOT in requeirements:
            requeirements.remove(HYPEN_E_DOT)
    return requeirements

setup(
    name="mlproject",
    version="0.0.1",
    author="ceren",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)


""" 
setup.py ve requirements.txt dosyaları aynı dizinde (örneğin, mlproject içinde) bulunuyor. 
Bu durumda, "requirements.txt" dosyasına yalnızca dosya adı olarak erişebilirsiniz çünkü dosya mevcut çalışma dizininde yer alır.

"""