# -*- coding: utf-8 -*-
"""
Created on Thu May  5 10:33:11 2022

@author: yamil
"""

palabra=input('ingrese palabra:')

if palabra[::-1]==palabra:
    print('la cadena',palabra,'es palindromo')
else:
    print('no es palindromo')