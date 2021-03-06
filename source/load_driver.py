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


def load_driver_py(driver_file):
    """
    Load the driver dictionary from an input python file.

    This returns the driver dictionary.
    """
    driver_module = driver_file.split('.')[0]
    exec('from %s import driver' % driver_module)
    return driver

def load_driver_json(driver_file):
    """
    Load the driver file that is in json format.

    This opens a json text file and returns a dictionary.
    """
    import json         # import the library that can read the driver file
    import collections  # use OrderedDict to keep the dictionary keys in the same order as they are in the .json file

    f = open(driver_file)
    driver = json.load(f, object_pairs_hook=collections.OrderedDict)
    f.close()

    return driver
