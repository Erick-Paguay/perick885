# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 19:27:04 2020
@author: SEDMQ
"""


import numpy
import random 

ejecutar=True

while ejecutar:
    
    dimensiones=int(input("Ingrese las dimensiones del vector mayor a 3 y menor que 30, o 999 para salir: "))
    if dimensiones == 999:
        ejecutar=False
        break
    if not (dimensiones >= 3 and dimensiones <= 30):
        print("El valor ingresado es incorrecto")
        continue
    arreglo=[int() for ind0 in range (dimensiones)]
    
    opcion=input("Si usted va a trabajar con numeros digite n, o digite l para letras: ")
    if not (opcion == "n" or opcion == "l" or opcion == "N" or opcion == "L"):
        print("El valor ingresado es incorrecto")
        continue
    
    if opcion == "n" or opcion == "N":
        #arreglo = numpy.zeros(dimensiones)
        for index in range(0,len(arreglo)):
            arreglo[index]=random.randint(1, 99)
    else:
        #arreglo = numpy.empty(dimensiones)
        for index in range(0,len(arreglo)):
            arreglo[index]=input("Ingrese valor del elemento: ")
                
            
       
    print(arreglo)
    opcionOrdenamiento=int(input("Ingrese 1 para ordenar de menor a mayor o 0 para ordenar de mayor a menor: "))
    if not (opcionOrdenamiento== 0 or opcionOrdenamiento==1):
        print("El valor ingresado es incorrecto,se los ordenara de menor a mayor ")
        opcionOrdenamiento=1
        
    arregloOrdenado=False
    while arregloOrdenado == False:
        arregloOrdenado = True
        for i in range(len(arreglo)-1):
            if opcionOrdenamiento == 1:
                if arreglo [i] > arreglo [i+1]:
                    aux = arreglo[i]
                    arreglo[i] = arreglo[i+1]
                    arreglo[i+1] = aux
                    arregloOrdenado = False
            else:
                 if arreglo [i] < arreglo [i+1]:
                    aux = arreglo[i]
                    arreglo[i] = arreglo[i+1]
                    arreglo[i+1] = aux
                    arregloOrdenado = False
        
    print(arreglo)
