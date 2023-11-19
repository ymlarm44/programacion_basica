# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 09:52:40 2022

@author: yamil
"""

def fibonacci(n):
    lista=[1,1]
    while len(lista)<n:
        for i in range(n):
            a=lista[i]+lista[i+1]
            lista.append(a)
    lista.pop()
    lista.pop()
    return(lista)

n=int(input('ingrese longitud de serie fibonacci:'))
serie=fibonacci(n)
print(serie)