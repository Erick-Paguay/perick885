# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 12:07:17 2020

@author: SEDMQ
"""


import numpy as np
matrix = np.array([[1,2,3,4,5], [6,7,8,9,10]], dtype = np.int64)
print (matrix)
print("\n"*2)
unos=np.ones((5,5))
print (unos)
print("\n"*2)
ceros=np.zeros((5,5))
print(ceros)
print("\n"*2)
ran=np.random.random((4,4))
print(ran)
print("\n"*2)
ept=np.empty((5,5))
print(ept)
print("\n"*2)
full=np.full((5,5),5)
print(full)
print("\n"*2)
espacio1=np.arange(0,100+1,5)
print(espacio1)
print("\n"*2)
espacio2=np.linspace(1,100,10)
print(espacio2)
print("\n"*2)