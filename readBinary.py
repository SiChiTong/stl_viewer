# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 20:42:24 2016

@author: don
"""

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from utilities import vec3d, triangle

#I'm trying to read floats from an STL binary file (http://en.wikipedia.org/wiki/STL_(file_format)#Binary_STL).

def read_binary_STL_file(STL_filename, facet, x_min, x_max, y_min, y_max, z_min, z_max):
    file = QFile("./stl/" + STL_filename)
    file.open(QIODevice.ReadOnly)
    
    file.seek(0)
    In = QDataStream(file)
    #In.setVersion(QDataStream.Qt_4_0)
    In.setByteOrder(QDataStream.LittleEndian)
    In.setFloatingPointPrecision(QDataStream.SinglePrecision)
    
    
    if(In.status() == QDataStream.Ok):
        file.seek(80)
        numberOfTriangles = In.readUInt32() #4bytes
        print "Number of Triangles: %d"% numberOfTriangles
            
        tri = triangle()
            
        x_max =  1e+30
        x_min = -1e+30

        y_max =  1e+30
        y_min = -1e+30

        z_max =  1e+30
        z_min = -1e+30
            
        for count in range(numberOfTriangles):
            file.seek(84 + count*50 + 0 + 0)
            temp_float_var = In.readDouble()  #4bytes
            tri.normal.x = temp_float_var
            
            file.seek(84 + count*50 + 0 + 4)
            temp_float_var = In.readDouble()  #4bytes
            tri.normal.y = temp_float_var
            
            file.seek(84 + count*50 + 0 + 8)
            temp_float_var = In.readDouble()  #4bytes
            tri.normal.z = temp_float_var
                
            #No using loops for memory issues
            file.seek(84 + count*50 + 12 + 0)
            temp_float_var = In.readDouble()  #4bytes
            tri.points[0].x = temp_float_var
            
            file.seek(84 + count*50 + 12 + 4)
            temp_float_var = In.readDouble()  #4bytes
            tri.points[0].y = temp_float_var
            
            file.seek(84 + count*50 + 12 + 8) 
            temp_float_var = In.readDouble()  #4bytes
            tri.points[0].z = temp_float_var
            
            file.seek(84 + count*50 + 24 + 0)
            temp_float_var = In.readDouble()  #4bytes
            tri.points[1].x = temp_float_var
            
            file.seek(84 + count*50 + 24 + 4)
            temp_float_var = In.readDouble()  #4bytes
            tri.points[1].y = temp_float_var
            
            file.seek(84 + count*50 + 24 + 8) 
            temp_float_var = In.readDouble()  #4bytes
            tri.points[1].z = temp_float_var

            file.seek(84 + count*50 + 36 + 0)
            temp_float_var = In.readDouble()  #4bytes
            tri.points[2].x = temp_float_var
            
            file.seek(84 + count*50 + 36 + 4)
            temp_float_var = In.readDouble()  #4bytes
            tri.points[2].y = temp_float_var
            
            file.seek(84 + count*50 + 36 + 8) 
            temp_float_var = In.readDouble()  #4bytes
            tri.points[2].z = temp_float_var                        

            file.seek(84 + count*50 + 48)
            control_bytes = In.readUInt16()   #2bytes
            
            
            print "Triangle %d"%(count+1)
            print "point 1 %f, %f, %f"%(tri.points[0].x, tri.points[0].y, tri.points[0].z)
            print "point 2 %f, %f, %f"%(tri.points[1].x, tri.points[1].y, tri.points[1].z) 
            print "point 3 %f, %f, %f"%(tri.points[2].x, tri.points[2].y, tri.points[2].z)               
            print            
            
            if (tri.points[0].x < x_min): x_min = tri.points[0].x
            if (tri.points[0].x > x_max): x_max = tri.points[0].x
            if (tri.points[0].y < y_min): x_min = tri.points[0].y
            if (tri.points[0].y > y_max): x_max = tri.points[0].y
            if (tri.points[0].z < z_min): x_min = tri.points[0].z
            if (tri.points[0].z > z_max): x_max = tri.points[0].z

            if (tri.points[1].x < x_min): x_min = tri.points[1].x
            if (tri.points[1].x > x_max): x_max = tri.points[1].x
            if (tri.points[1].y < y_min): x_min = tri.points[1].y
            if (tri.points[1].y > y_max): x_max = tri.points[1].y
            if (tri.points[1].z < z_min): x_min = tri.points[1].z
            if (tri.points[1].z > z_max): x_max = tri.points[1].z
                    
            if (tri.points[2].x < x_min): x_min = tri.points[2].x
            if (tri.points[2].x > x_max): x_max = tri.points[2].x
            if (tri.points[2].y < y_min): x_min = tri.points[2].y
            if (tri.points[2].y > y_max): x_max = tri.points[2].y
            if (tri.points[2].z < z_min): x_min = tri.points[2].z
            if (tri.points[2].z > z_max): x_max = tri.points[2].z
                


            facet.append(tri)                        
                
        return True    #Success
    else:
        print "ERROR: Input STL file could not be opened !"
        
def getGeometryInput(facet, x_min, x_max, y_min, y_max, z_min, z_max, arg): #recode with support with binary and ascii    
    STL_filename = arg
    print STL_filename
    print type(STL_filename)
    #STL_file_path = "../stl/"
    
    status = read_binary_STL_file(STL_filename, facet, x_min, x_max, y_min, y_max, z_min, z_max)
    
    if status == False:
        return status
    else:
        print "X range: %f  to %f    (delta= %f)"%( x_min, x_max, x_max - x_min)
        print "Y range: %f  to %f    (delta= %f)"%( y_min, y_max, y_max - y_min)
        print "Z range: %f  to %f    (delta= %f)"%( z_min, z_max, z_max - z_min)
        
        return status
        

if __name__ =='__main__':
    import sys
    
    facet = []
    x_min = 0
    x_max = 0
    y_min = 0
    y_max = 0
    z_min = 0
    z_max = 0
    
    getGeometryInput(facet, x_min, x_max, y_min, y_max, z_min, z_max, sys.argv[1])
    
    print "Triangle %d"%(len(facet) + 1)
    print "point 1 %f, %f, %f"%(facet[len(facet)].points[0].x, facet[len(facet)].points[0].y, facet[len(facet)].points[0].z)              
    print 
    