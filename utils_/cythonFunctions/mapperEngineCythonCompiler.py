from distutils.core import setup
from Cython.Build import cythonize
import cython
setup(
      name = "mapperEngineCython",
      ext_modules = cythonize('mapperEngineCython.pyx',language_level = "3")
)
@cython.Locals(

)
def maperBNF(bnf,individues):
      lineasBNF=bnf.split("\n")
