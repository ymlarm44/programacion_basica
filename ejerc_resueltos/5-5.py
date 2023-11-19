# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 19:33:43 2022

@author: yamil
"""
'''5. Leer N datos numéricos. Obtener la media (M) y
 la desviación estándar (DS) de la lista. '''
lista=[]
n=int(input('ingrese un dato:'))
lista.append(n)
print('para finalizar ingrese "999"')
while n!=999:
    n=int(input('ingrese un dato:'))
    lista.append(n)
lista.pop()
print('los datos ingresados son',lista)
suma=0
dist=0
for x in lista:
    suma=x+suma
media=round((suma/len(lista)),2)
for d in lista:
    (d-media)**2
    dist=dist+d
ds=round(((dist/len(lista))**0.5),2)
print('la media es',media)
print('la desviacion estandar es',ds)
