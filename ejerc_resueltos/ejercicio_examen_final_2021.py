# -*- coding: utf-8 -*-
"""
Created on Mon May 23 20:13:53 2022

@author: yamil
"""

c=12
f=8
matriz=[([0]*c)for i in range(f)]

archivo=open('VENTAS2020.txt')
registro=archivo.readlines()
archivo.close()

#A)
for i in registro:
    mes,sucursal,venta=i.split(sep=',')
    venta=int(venta.strip('\n'))
    mes=int(mes)
    sucursal=int(sucursal)
    matriz[sucursal-1][mes-1]+=venta

import mostrarmatriz as m
m.mostrarmatriz(matriz)

#B)
print('ventas suc 7:',sum(matriz[6]))

#C)
maximo=0
sucmax=0
for i in range(len(matriz)):
    if matriz[i][2]>maximo:
        maximo=matriz[i][2]
        sucmax=i+1
print('mayor venta en marzo:',maximo,'en sucursal:',sucmax)
