# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 10:53:23 2022

@author: yamil
"""

import operaciones_naturales as op

n=int(input('ingrese un numero:'))

if op.es_par(n)==True:
    print(n,'es par')
else:
    print(n,'no es par')

if op.es_primo(n)==True:
    print(n,'es primo')
else:
    print(n,'no es primo')
    
print('los divisores de',n,'son',op.divisores(n))
print('el factorial de',n,'es',op.factorial(n))

    