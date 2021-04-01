from distutils.core import setup
from Cython.Build import cythonize
import pyximport
import Cython.Compiler.Options
Cython.Compiler.Options.annotate = True
pyximport.install(setup_args={"script_args":["--compiler=msvc"]}, reload_support=True)

setup(
      name = "ga",
      ext_modules = cythonize('ga.pyx',language_level = "3", annotate=True)
)

#setup(
#      name = "population",
#      ext_modules = cythonize('population.pyx',language_level = "3", annotate=True)
#)
#python maper.py build_ext --inplace --compiler=msvc --force
