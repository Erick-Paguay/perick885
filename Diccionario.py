# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 11:13:25 2020

@author: SEDMQ
"""


ipadd={"R1":"10.0.0.1","R2":"10.0.0.2",
       "R3":"10.0.0.3","S1":"10.1.0.1",
       "S2":"10.1.0.2"}
print(type(ipadd))
dict1={"usuario1":"1753903788","valor":5000,"edad":18,
       "soltero :C":True,"Rate en %":52.2}
print(dict1)
print(ipadd ['S2'])
ipadd ['S5']="4.2.8.4"
print("S1" in ipadd)
print("edad" in dict1)



