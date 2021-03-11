from distutils.core import setup
from Cython.Build import cythonize
import cython
setup(
      name = "maperEngineCython",
      ext_modules = cythonize('maperEngineCython.pyx',language_level = "3")
)
@cython.Locals(

)
def maperBNF(bnf,individues):
      lineasBNF=bnf.split("\n")
