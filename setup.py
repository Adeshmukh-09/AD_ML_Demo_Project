from setuptools import find_packages,setup ## it checks the whole application folder where ever it find packages it maps them.
from typing import List ## this will help us to get list of the required library from requirements.txt file.

HYPHEN_E_DOT= '-e .'

def get_requirements(file_path:str)->List[str]:
## this function will return the list of requirements from requirements.txt.
    requirements=[] ## in this the list will get saved.
    with open(file_path) as file_obj: ## this will read the requirements that we have entered in the requirements.txt file.
        requirements=file_obj.readlines() ## this will read the lines from the requirements.txt file.
        requirements=[req.replace('\n',"")for req in requirements] ## this line of code do is that it will go th the requirements.txt file ##and it will check for each line but at eah line we have one difference that is of \n so we ahve to ignore right so we are doing ##that here and replacing it with space so that everytime it will loop from the new line.
        if HYPHEN_E_DOT in requirements:
           requirements.remove(HYPHEN_E_DOT)
        
    return requirements

setup(
    name='DemoMLproject',
    version='0.0.1',
    author='arjundeshmukh',
    author_email='arjundeshmukh757575@gmail.com', ## this setup functiion gives us the basic information of our app.
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt') ## this is used to istall the required libraries or packahges that we want. Now ##al teh time we will ##insert some new libraries right to make it dynamic we will use get_requirements function. 
)
