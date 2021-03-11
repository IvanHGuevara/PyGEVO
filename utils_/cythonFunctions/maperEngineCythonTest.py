
#python maperEngineCython.py build_ext --inplace --compiler=msvc --force
from utils_.cythonFunctions import maperEngineCython

maperEngineCython.mapBNF(1000000000)