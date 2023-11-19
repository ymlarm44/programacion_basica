# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 16:19:58 2022

@author: yamil
"""

''' 1. Escriba un programa en Python donde el
 usuario ingrese un número natural positivo 
 y muestre por consola todos los valores 
 impares desde 1 hasta el número ingresado.'''
 
numero=int(input('ingrese un numero natural:'))

print('los numeros impares hasta',numero,'son:')

for val in range(1,numero+1):
    if val%2!=0:
        print (val)
print('fin')        