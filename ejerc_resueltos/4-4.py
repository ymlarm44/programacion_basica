# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 19:07:48 2022

@author: yamil
"""

from random import randint
lista=[]
nunicos=0
for i in range(15):
    lista.append(randint(0,9))
print('la lista es',lista)
for x in lista:
    if lista.count(x)<2:
        nunicos=nunicos+1
print('la cantidad de numeros unicos en la lista es',nunicos)