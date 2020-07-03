# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 17:29:53 2020

@author: SEDMQ
"""


def isYearLeap(year):
    
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    else:
        return False

def daysInMonth(year, month):

    if isYearLeap(year) and month == 2:
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
		print("Nice dick")
	else:
		print("Failed")