# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 11:38:07 2020

@author: TU PAPI RICO
"""


nombre=input("Ingresa tu nombre: ")
apellido=input("Ingresa tu apellido: ")
ubicacion=input("Ingresa tu ubicacion: ")
str1 = int ( input ("Ingrese su edad: "))
if str1 >= 1 and str1 < 5:
    print("Es un bebe") 
elif str1 >= 5 and str1 < 12:
    print("Es un niño") 
elif str1 >= 12 and str1 < 18:
    print("Es un adolecente") 
elif str1 >= 18 and str1 < 60:
    print("Es un adulto") 
elif str1 >= 60 and str1 <= 1000:
    print("Es un adulto mayor") 
else:
    print("No esta en el rango")
