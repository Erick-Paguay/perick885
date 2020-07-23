# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 17:23:42 2020

@author: Erick Paguay 
"""
import numpy
import random 

filas=int(input("Ingrese cuantas filas requiere: "))
columnas=int(input("Ingrese cuantas columnas requiere: "))
matrix=numpy.zeros((filas,columnas))
matrixDiagonal=numpy.zeros((filas,columnas))
matrixDiagonalSecundaria=numpy.zeros((filas,columnas))

for ixFila in range(0,filas):
    for ixColumna in range(0,columnas):
        matrix[ixFila][ixColumna]=random.randint(1, 99)  
print(matrix)

for ixFila in range(0,filas):
    for ixColumna in range(0,columnas):
        if ixFila == ixColumna:
            matrixDiagonal[ixFila][ixColumna]=matrix[ixFila][ixColumna] 
print("El valor de la diagonal principal de la matriz es:  ")
print(matrixDiagonal)
aux=columnas-1
for ixFila in range(0,filas):
    for ixColumna in range(0,columnas):
        if ixColumna == aux:
            matrixDiagonalSecundaria[ixFila][ixColumna]=matrix[ixFila][ixColumna] 
    aux=aux-1 
print("El valor de la diagonal secundaria de la matriz es:  ")
print(matrixDiagonalSecundaria)






    
     
