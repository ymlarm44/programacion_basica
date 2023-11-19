# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 17:36:23 2022

@author: alumno
"""

from random import random
lista=[]
lista2=[]
for i in range(1000):
    lista.append(round(random(),2))

for i in lista:
    c=lista.count(i)
    if (i,c) not in lista2:
        lista2.append((i,c))
print(lista2)