# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 10:07:11 2022

@author: yamil
"""

from random import random
secuencia=[]
for i in range(1000):
    n=round(random(),2)
    secuencia.append(n)

listado=[]
for i in secuencia:
    c=secuencia.count(i)
    if (i,c) not in listado:
        listado.append((i,c))

print(listado)