# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 18:25:48 2022

@author: alumno
"""

f=4
c=25
matriz=[([0]*c)for i in range(f)]

sucursal=int(input('ingrese numero de sucursal:'))

while sucursal !=0:
    art=int(input('ingrese codigo de articulo:'))
    ventas=int(input('¿cuantas ventas se hicieron de dicho articulo?:'))
    matriz[sucursal-1][art-1]=ventas
    sucursal=int(input('ingrese numero de sucursal:'))


'''
for i in range(f):
    for j in range(c):
        ventas=int(input())
        matriz[i][j]=ventas
'''

#b)
b=sum(matriz[2])

#c)
c=matriz[0][5]
