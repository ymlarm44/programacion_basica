# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 16:05:06 2022

@author: yamil
"""

lista=[]
for i in range(100):
    if i%3==0 and len(lista)<20:
        lista.append(i)
print('los primeros 20 multiplos de 3 son',lista)

multiplos=[x*3 for x in range(20)]
print('los primeros 20 multiplos de 3 son',multiplos)
