# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 21:46:29 2016

@author: don
"""

class vec3d(object):
    def __init__(self):
        super(vec3d, self).__init__()
        self.x = 0
        self.y = 0
        self.z = 0        
        
 #   def __init__(self, x, y, z):
 #       super(vec3d, self).__init__()
 #       self.x = x
 #       self.y = y
 #       self.z = z
        
 #   def __init__(self, vec):
 #       super(vec3d, self).__init__()
 #       self.x = vec.x
 #       self.y = vec.y
 #       self.z = vec.z
        
class triangle(object):
    def __init__(self):
        super(triangle, self).__init__()
        self.normal = vec3d()        
        self.points = [vec3d(), vec3d(), vec3d]
        
 #   def __init__(self, normal, *points):
 #       super(triangle, self).__init__()        
 #       self.normal = vec3d()
 #       self.points = []

  #      self.normal = normal
  #      for point in points:
  #          self.points.append(point)
            
  #  def __init__(self, tri):
  #      super(triangle, self).__init__()
  #      self.normal = tri.normal
  #      self.points = tri.points