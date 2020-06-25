# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 14:57:26 2020

@author: SEDMQ
"""


#Python 3 
primeraEvaluacion=float(input("Ingrese su primera evaluación:"))
segundaEvaluacion=float(input("Ingrese su segunda evaluación:"))
terceraEvaluacion=float(input("Ingrese su tercera evaluación:"))
peorNota=0
if primeraEvaluacion >= segundaEvaluacion :
    if segundaEvaluacion >= terceraEvaluacion:
        peorNota=terceraEvaluacion
    else: 
        peorNota=segundaEvaluacion
elif primeraEvaluacion >= terceraEvaluacion :
    peorNota=terceraEvaluacion
else: 
    peorNota=primeraEvaluacion
notaTotal=primeraEvaluacion+segundaEvaluacion+terceraEvaluacion-peorNota
print("Tu nota total es :",notaTotal)
