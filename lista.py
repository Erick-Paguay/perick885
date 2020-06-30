# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 11:12:05 2020

@author: SEDMQ
"""
switch=[]
router=[]
lista=["R1","R2","R3",
       "R4","S1","S2","S3"]
for i in lista:
    if "S" in i :
        switch.append(i)
    else:
            router.append(i)
print(switch)
print(router)
        
        