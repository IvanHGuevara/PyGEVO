import glob
import os
from os import remove
from distutils.core import setup
from Cython.Build import cythonize
import pyximport
import Cython.Compiler.Options
Cython.Compiler.Options.annotate = False #html
pyximport.install(setup_args={"script_args":["--compiler=msvc"]}, reload_support=True)




path=os.getcwd()
print(path)
files=[]
dist=""
for i in range(0,5):

    targetPattern = path+"//"+dist+"*.pyx"
    files=files+glob.glob(targetPattern)
    dist = dist + "**//"
for file in files:
    print("Compile:",end="")
    print(file)
    pathAnterior=os.getcwd()

    name=file.split("\\")[-1]
    print(name)
    simpleName=name.replace(".pyx", "")
    path=file.replace(name,"")
    os.chdir(path)
    setup(name=simpleName,ext_modules=cythonize(name, language_level="3", annotate=False))
    #remove(simpleName+".c")
    #remove(simpleName + ".**.pyd")
    #remove(simpleName + ".html")
    os.chdir(pathAnterior)
    print("-------------------------------------------------------------------------------------------------------------")