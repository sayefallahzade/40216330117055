# -*- coding: utf-8 -*-
"""Untitled6.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ao_VTciYWGIpsMvmWDOx6WbslJaChPH3
"""

import math
class circle ():
  p=math.pi
  def __init__(self,r=5):
     self.rad=r
     print("circle created ")
  def Perim(self):
   p=math.pi
   return 2*p*self.rad
  def Area(self):
   p=math.pi
   return p*self.rad*self.rad
  def __del__(self):
    print("circle deleted ")
    return -1


k=circle(10)
print (k.Perim())
print (k.Area())
print (k.p)
print (k.rad)
del k