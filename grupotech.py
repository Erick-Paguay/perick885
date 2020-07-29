# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 19:27:04 2020
@author: Erick Paguay
"""


if __name__ == '__main__':
	inicial = int()
	final = int()
	impresiones = int()
	blanconegro = str()
	costoblanconegro = float()
	costocolor = float()
	costoimpresion = float()
	costoblanconegro = 0.06
	costocolor = 0.12
	print("Contador inicial: ")
	inicial = int(input())
	print("Contador final: ")
	final = int(input())
	print("Ingrese 1 si fue impresion blanco y negro y 2 si fue a color: ")
	blanconegro = input()
	if not (blanconegro=="1" or blanconegro=="2"):
		print("Tipo de impresion incorrecto")
	else:
		if final<inicial:
			print("El valor final es mayor que el inicial")
		else:
			impresiones = final-inicial
			if blanconegro=="1":
				costoimpresion = impresiones*costoblanconegro
			else:
				costoimpresion = impresiones*costocolor
print("Impresiones: ",impresiones)
print("Costo: ",costoimpresion)

