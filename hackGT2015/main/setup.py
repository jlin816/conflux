from distutils.core import setup
from Cython.Build import cythonize

setup(
  name = 'radii',
  ext_modules = cythonize("radii.pyx"),
)