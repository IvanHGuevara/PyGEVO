from subprocess import call
import os
def compiler():
    pathAnterior=os.getcwd()
    path=pathAnterior.split("PyGE")[0]+"PyGE//"
    os.chdir(path)
    call("python setupAll.py build_ext --inplace")
    os.chdir(pathAnterior)
