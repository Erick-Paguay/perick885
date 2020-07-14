# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 11:58:29 2020

@author: SEDMQ
"""


import numpy as np
a=np.array([(1,2,3),(4,5,6)])
b=np.array([(1,2,3),(4,5,6)])
print(a+b,"\n")
print(a-b,"\n")
print(a*b,"\n")
print(a/b,"\n")
c=np.ones((4,4))
print(c,"\n")
d=np.ones((4,2))
print(d,"\n")
print(c.dot(d),"\n")
print(np.dot(c,d),"\n")

