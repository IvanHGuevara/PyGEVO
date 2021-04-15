from subprocess import call
import os
def compiler():
    pathAnterior=os.getcwd()
    call("python setupAll.py build_ext --inplace")
    os.chdir(pathAnterior)
