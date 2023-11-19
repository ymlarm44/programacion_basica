# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 17:09:31 2022

@author: alumno
"""

n=int(input('cantidad de numeros a ingresar:'))

numero=int(input('ingrese un numero:'))
menor=numero
mayor=numero
suma=numero

for val in range(1,n):
    numero=int(input('ingrese un numero:'))
    suma=suma+numero
  
    if numero>mayor:
        mayor=numero
    if numero<menor:
        menor=numero

media=int(suma/n)

print('el mayor es:',mayor)
print('el menor es:',menor)
print('la media es:',media)
