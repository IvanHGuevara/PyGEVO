from subprocess import call
import os
def compiler():
    pathAnterior=os.getcwd()
    path="utils_/cythonFunctions/"
    os.chdir(path)
    call("python mapperSetup.py build_ext --inplace")
    call("python populationSetup.py build_ext --inplace ")
    os.chdir(pathAnterior)
