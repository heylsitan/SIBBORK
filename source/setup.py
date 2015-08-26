"""
 SIBBORK is an individual-based spatially-explicit gap dynamics model for simulation of forests, here specifically tailored to boreal forests in Siberia.
    Copyright (C) 2015  Ksenia Brazhnik

    This program is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation; either version 2 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License along
    with this program; if not, write to the Free Software Foundation, Inc.,
    51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
"""


from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
import numpy

ext_options = {
               "sources": ["light3d.pyx"],
               }

extmodule = Extension("light3d",["light3d.pyx"],include_dirs=["/Applications/Canopy.app/appdata/canopy-1.5.5.3123.macosx-x86_64/Canopy.app/Contents/lib/python2.7/site-packages/numpy/core/include/"])
#extmodule = Extension("light3d", **ext_options,include_dirs=["/Applications/Canopy.app/appdata/canopy-1.5.5.3123.macosx-x86_64/Canopy.app/Contents/lib/python2.7/site-packages/numpy/core/include/"])
# Building
setup(
    name = 'light3d',
    version = '1.0',
    description = 'Cythonized Light3D routine.',
    author = "Author Here",
    long_description = 'This python package is a faster implementation of the 3D light ray tracing subroutine.',
    ext_modules = [extmodule],
    cmdclass = {'build_ext': build_ext},
)                                  

