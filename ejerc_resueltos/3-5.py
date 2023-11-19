# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 09:48:05 2022

@author: yamil
"""

''' 5. Diseñe e implemente un programa en Python que lea un número entero 
e informe si es primo o no. '''

numero=int(input('ingrese un numero entero:'))
cantidad_multiplos=0

for val in range(1,numero+1):
    if numero%val==0:
        cantidad_multiplos=cantidad_multiplos+1
    elif cantidad_multiplos==3:
        break

if cantidad_multiplos==2:
    print('el numero',numero,'es primo')
elif cantidad_multiplos>2:
    print('el numero',numero,'no es primo')
        
    