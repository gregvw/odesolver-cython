from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
import numpy
import os
os.environ["CC"] = "gcc"
os.environ["CXX"] = "g++"
setup( name = 'forward_euler',
ext_modules=[Extension("forward_euler",
sources=["forward_euler.pyx"],
language="c++",
extra_compile_args=["-std=c++11"],
include_dirs=[numpy.get_include()])],
cmdclass = {'build_ext': build_ext},
) 
