from subprocess import call
import os
def compiler():
    lastPath=os.getcwd()
    path = os.path.realpath('../../utils_/search_operators/')

    print(path)
    os.chdir(path)
    call("python setupAll.py build_ext --inplace")
    os.chdir(lastPath)
