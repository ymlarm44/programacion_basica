# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 08:13:19 2022

@author: yamil
"""

def tipo(a):
    for i in range(2,a):
        if a%i==0:
            a=False
        else:
            a=True
    return(a)

numero=int(input('numero:'))
x=tipo(numero)
print(x)

otro_numero=int(input('otro numero:'))
y=tipo(otro_numero)
print(y)