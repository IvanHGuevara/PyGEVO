#python maperSetup.py build_ext --inplace --compiler=msvc --force
from subprocess import call
call("python populationSetup.py build_ext --inplace --compiler=msvc")