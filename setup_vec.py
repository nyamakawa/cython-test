from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
import numpy

ext_modules=[
    Extension("vec_cy",
              ["vec_cy.pyx"],
              libraries=["m"]) # Unix-like specific
]

setup(
  name = "Demos",
  cmdclass = {"build_ext": build_ext},
  ext_modules = ext_modules,
  include_dirs = [numpy.get_include()]
)