# -*- coding: utf-8 -*-
"""Untitled4.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ao_VTciYWGIpsMvmWDOx6WbslJaChPH3
"""

class A ():
    name="ali"
    age=25

A.name="reza"
print (A.name)

test=A()
test.name="ahmad"
print(test.age)

print(getattr(A,"name"))
setattr(A,"name","hasan")