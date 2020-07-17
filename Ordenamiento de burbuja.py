# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 19:27:04 2020

@author: SEDMQ
"""


import numpy
import random 

dimensiones=int(input("Ingrese las dimensiones: "))
arreglo = numpy.zeros(dimensiones)


for index in range(0,len(arreglo)):
    arreglo[index]=random.randint(1, 99)
    
print(arreglo)
    
arregloOrdenado=False
while arregloOrdenado == False:
    arregloOrdenado = True
    for i in range(len(arreglo)-1):
        if arreglo [i] < arreglo [i+1]:
             aux = arreglo[i]
             arreglo[i] = arreglo[i+1]
             arreglo[i+1] = aux
             arregloOrdenado = False
    
print(arreglo)