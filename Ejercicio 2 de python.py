# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 14:30:54 2020

@author: SEDMQ
"""


#Python 2 
horasTrabajadas=int(input("Ingrese las horas trabajadas:"))
costoHora=float(input("Ingrese el costo de hora:"))
descuento=float(input("Ingrese el descuento:"))
honorario=costoHora*horasTrabajadas
bono=0
if horasTrabajadas > 40 :
    bono=costoHora*0.5*(horasTrabajadas-40)
print("Tu pago semanal es :",(honorario+bono-descuento))