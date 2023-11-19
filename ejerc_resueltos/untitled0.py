# -*- coding: utf-8 -*-
"""
Created on Thu May  5 15:35:50 2022

@author: yamil
"""

from statistics import pstdev

muestra=int(input('ingrese tamaño de la muestra:'))
lista=[]

for i in range(muestra):
    n=int(input('ingrese numero:'))
    lista.append(n)

sumatoria=0
for i in lista:
    sumatoria=sumatoria+i
media=sumatoria/muestra
print('media:',media)

desvio=pstdev(lista)
print('desvio:',desvio)