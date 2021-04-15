import glob
import os
import platform
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
system = platform.system()

for i in range(0,5):
    targetPattern = path+"//"+dist+"*.pyx"
    files=files+glob.glob(targetPattern)
    dist = dist + "**//"

for file in files:
    print("Compile:",end="")
    print(file)
    pathAnterior=os.getcwd()
    if system=="Windows":
        name = file.split("\\")[-1]
    else:
        name = file.split("/")[-1]
    simpleName=name.replace(".pyx", "")
    path=file.replace(name,"")
    os.chdir(path)
    setup(name=simpleName,ext_modules=cythonize(name, language_level="3", annotate=False))
    os.chdir(pathAnterior)
    print("-------------------------------------------------------------------------------------------------------------")