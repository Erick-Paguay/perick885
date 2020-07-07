# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 17:38:41 2020

@author: SEDMQ
"""

import datetime
def IsYearLeap(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    else:
        return False

def daysInMonth(year, month):

    if IsYearLeap(year) and month == 2:
        return 29
    elif month == 2:
        return 28
    elif month in [4, 6, 9, 11]:
        return 30
    else: 
        return 31
        

testYears = [1900, 2000, 2016, 1987]
testMonths = [2, 2, 1, 11]
testResults = [28, 29, 31, 30]
for i in range(len(testYears)):
	yr = testYears[i]
	mo = testMonths[i]
	print(yr, mo, "->", end="")
	result = daysInMonth(yr, mo)
	if result == testResults[i]:
		print("Ok")
	else:
		print("Failed")

def Validate(date_text):
    valido=False 
    try:
        datetime.datetime.strptime(date_text, '%Y-%m-%d')
        valido=True
    except :
        print ("None:Incorrect date")
    return valido


year = int(input("Digite un año:"))
month = int(input("Digite un mes:"))
day = int(input("Digite un dia:"))
date=str(year)+"-"+ str(month)+"-"+str(day)

isCorrectDate=Validate(date)
if isCorrectDate :
    if IsYearLeap(year) :
        print("The year has 366 days")
    else:
        print("The year has 365 days")



