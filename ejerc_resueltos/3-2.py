# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 11:06:04 2022

@author: yamil
"""

''' 2. Escriba un programa en Python donde el usuario ingrese números naturales,
 se sumen y se muestre el resultado por pantalla. Para que el usuario deje 
 de añadir números a la suma debe ingresar el valor -1 '''
 
suma=1
numero=1
while numero!=-1:
    numero=int(input('ingrese un numero:'))
    suma=suma+numero
print('la suma es:',suma)
