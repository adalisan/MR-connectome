from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

import numpy

ext_modules = [Extension("fiber",["fiber.pyx"],include_dirs=[numpy.get_include()]),
               Extension("roi",["roi.pyx"],include_dirs=[numpy.get_include()]),
               Extension("fibergraph",["fibergraph.pyx"],include_dirs=[numpy.get_include()]),
]
# You can add directives for each extension too
# by attaching the `pyrex_directives`
for e in ext_modules:
    e.pyrex_directives = {"boundscheck": False}
setup(
    name = "cython accelerator for processing MRCAP graphs",
    cmdclass = {"build_ext": build_ext},
    ext_modules = ext_modules
)