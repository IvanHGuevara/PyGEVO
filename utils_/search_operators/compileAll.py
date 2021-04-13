from subprocess import call
import os
def compiler():
    pathAnterior=os.getcwd()

    #path=os.path.realpath('../../utils_/search_operators/')
    path = os.path.realpath('../../utils_/search_operators/')

    print(path)
    os.chdir(path)
    #call("python mapperSetup.py build_ext --inplace")
    #call("python populationSetup.py build_ext --inplace")
    call("python setupAll.py build_ext --inplace")
    os.chdir(pathAnterior)
