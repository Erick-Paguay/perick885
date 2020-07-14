# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 12:17:45 2020

@author: SEDMQ
"""

matrix=[[0,0,0,0,0,0],[0,0,0,0,0,0],
        [0,0,0,0,0,0],[0,0,0,0,0,0],
        [0,0,0,0,0,0]]
for i in range(0,5):
    for j in range (0,6):
        print("Ingrese el valor para la posicion: ",i,j)
        matrix[i][j]=int(input())
print(matrix)
	