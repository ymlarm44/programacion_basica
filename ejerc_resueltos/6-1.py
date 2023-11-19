# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 08:07:01 2022

@author: yamil
"""

def div(a):
    divisores=[]
    for i in range(1,a+1):
        if a%i==0:
            divisores.append(i)
    return(divisores)

numero=div(9)
print(numero)
