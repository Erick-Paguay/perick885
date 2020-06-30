# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 11:39:05 2020

@author: SEDMQ
"""


def direccion(calle,sector,codigopostal,referencia,numcasa):
    print("Su direccion es: ","Su sector es: ",sector,"Calle",calle)
    print("Su casa es la #: ",numcasa,"Con codigo postal #: ",codigopostal)
    print("Y esta cerca de: ",referencia) 
print("Ingrese los datos que se solicitan de direccion: ")
c=input("Ingrese la calle: ")
s=input("Ingrese sector de residencia:: ")
cod=input("Ingrese su codigo postal: ")
r=input("Ingrese una referencia de su domicilio: ")
num=input("Ingrese el # de casa: ")

direccion(c,s,cod,r,num)