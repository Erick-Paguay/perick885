# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 13:58:07 2020

@author: SEDMQ
"""


finobacci=int(input("Ingrese un numero para realizar la sucesion: "))
contador = 1
numero = 1
base = 0
while(contador <= finobacci):
    print(base)
    numero_siguiente = numero + base
    base = numero
    numero = numero_siguiente
    contador += 1
