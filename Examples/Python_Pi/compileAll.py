from subprocess import call
import os
def compiler():
    pathAnterior=os.getcwd()
    #path="Examples/Python_Classify/"
    #os.chdir(path)
    #call("python mapperSetup.py build_ext --inplace")
    #call("python populationSetup.py build_ext --inplace")
    call("python setupAll.py build_ext --inplace")
    os.chdir(pathAnterior)
