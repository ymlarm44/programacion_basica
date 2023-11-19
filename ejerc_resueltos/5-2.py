# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 10:00:07 2022

@author: yamil
"""
tupla=(1,2,3,4,5,6,7,4,2,3,6,8,0,9,1,2,1,3)
repetidos=[]
for i in tupla:
    if tupla.count(i)>1 and i not in repetidos:
        repetidos.append(i)
print('los elementos repetidos son:',repetidos)
        