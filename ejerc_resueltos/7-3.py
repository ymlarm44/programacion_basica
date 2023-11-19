# -*- coding: utf-8 -*-
"""
Created on Wed May  4 09:50:57 2022

@author: yamil
"""

str=input('ingrese cadena:')

print('''menu:
      1. pasar a mayusculas
      2. pasar a minusculas
      3. primera mayuscula''')
      
opcion=input('opcion:')

if opcion=='1':
    print(str.upper())
elif opcion=='2':
    print(str.lower())
elif opcion=='3':
    print(str.capitalize())
else:
    print('opcion inexistente')
    