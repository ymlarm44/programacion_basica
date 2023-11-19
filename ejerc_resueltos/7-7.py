# -*- coding: utf-8 -*-
"""
Created on Thu May  5 15:58:40 2022

@author: yamil
"""

nombre=input('ingrese nombre:')
lista=[]
while nombre!='fin':
    lista.append(nombre)
    nombre=input('ingrese nombre:')

lista=sorted(lista)
for nombre in lista:
    print(nombre)