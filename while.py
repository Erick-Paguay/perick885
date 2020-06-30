# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 12:45:39 2020

@author: SEDMQ
"""


while True: 
    x=input("Ingrese un numero: ")
    if x=='q' or x=='quit':
        break    
else:
    x=int(x)
    y=1
    i=0
    while True:
        print (y)
        i+=y
        y=y+1
        if y>x:
            break
        print("La suma de los numeros del 1 al ",
              x," es: ",i)