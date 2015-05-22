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

import gdal

def generate_ERDASimg_grid (metadata_file,matrix_file,numpy_raster):
    """
    this function takes the GDD matrix created in via def DefGDD, 
    combines it with metadata from the input ascii file created in GIS, 
    and outputs the GDD matrix with the geospatial metadata
    in ascii format that can be read by into GIS
    Inputs: metadata_file -- .txt file generated in GIS via conversion to ASCII tool, 
                             has georeferenced metadata
            matrix_file -- .txt file generated here by combining metadata 
                           with matrix of variables
            numpy_raster -- matrix computed in pyzelig to be displayed in GIS
    Outputs: matrix_file -- combine metadata (georef) and pyzelig computed values
    """
    format = "HFA"
    driver = gdal.GetDriverByName( format )
    src_ds = gdal.Open( metadata_file )  #the georeferencing will be taken from the metadata_file
    dst_ds = driver.CreateCopy( matrix_file, src_ds, 0 ) #the GDD matrix will be written to the matrix_file, after the georef data is copied to it
    dst_ds.GetRasterBand(1).WriteArray( numpy_raster ) #this is where whatever numpy matrix I generate in pyzelig is written to a raster to display in GIS
