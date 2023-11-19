# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 17:32:17 2022

@author: yamil
"""
from random import randint
lista=[]
for i in range(10):
    lista.append(randint(1,100))
print('la lista es',lista)
lista.sort()
print('la lista ordenada creciente es',lista)