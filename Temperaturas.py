# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 12:44:02 2020

@author: Erick Paguay
"""


arregloTemperaturas=[]
temperaturas =int(input("Ingrese cantidad de temperaturas[1,10]: "))
if not (temperaturas>1 and temperaturas<10):
    print("El valor debe estar entre 1 y 10")
else:
    for i in range (temperaturas):
         temperatura= int(input("Temperatura en C°: "))
         arregloTemperaturas.append(temperatura)
    print(arregloTemperaturas)
    cgaseoso= 0
    cliquido = 0
    csolido = 0
    sumTemperaturas=0
    for valor in range(0,temperaturas):
        sumTemperaturas+=arregloTemperaturas[valor]
        if (arregloTemperaturas[valor]>=100) :
             cgaseoso+=1
        elif (arregloTemperaturas[valor]<=0):
             csolido += 1
        elif (arregloTemperaturas[valor]>0 and arregloTemperaturas[valor]<100):
             cliquido += 1
    promedioCelsius=sumTemperaturas/temperaturas
    promedioFarenheit=(promedioCelsius * 9/5) +32         
          
    print("RESUMEN DEL ANÁLISIS DE MUESTRAS DE AGUA")
    print("Cantidad de muestras sólidas: ", csolido)
    print("Cantidad de muestras líquidas: ", cliquido)
    print("Cantidad de muestras gaseosas: ", cgaseoso)
    print("Temperatura promedio en ° Celsius: ",promedioCelsius)
    print("Temperatura promedio en ° Farenheit: ",promedioFarenheit)