# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 09:31:35 2022

@author: yamil
"""

''' 4. Escriba un programa que pida un número entero mayor que cero y calcule
 su factorial. '''

numero=int(input('ingrese numero:'))
factorial=1
if numero>0:
    for val in range(numero,0,-1):
        factorial=val*factorial
print('el factorial de',numero,'es',factorial)
