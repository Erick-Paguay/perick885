# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 14:04:06 2020

@author: SEDMQ
"""
#Python1 
llantas=int(input("Ingrese la cantidad de llantas a comprar:"))
precio=float(input("Ingrese el precio unitario:"))
precioTotal=llantas*precio
descuento=0
if llantas > 4 :

    descuento=precioTotal*0.1 

print("El valor es:",(precioTotal-descuento))
