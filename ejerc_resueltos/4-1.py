# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 15:25:39 2022

@author: yamil
"""
lista=[]
for i in range(2,42):
    if i%2==0:
        lista.append(i)
print('los primeros',len(lista),'valores pares de la lista son:')
print(lista)
print('-------------------------------------------------------------------')
lista2=[]
for i in range (2,42):
    lista2.append(i)
print('los primeros 20 valores pares de la lista son:')
print(lista2[0:len(lista2):2])
