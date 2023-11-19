# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 23:22:18 2022

@author: yamil
"""
"""2. Escriba un programa que lea por consola el stock de cada uno de los 10 
productos que comercializa una empresa. Posteriormente, lea los 16 pares de 
datos correspondientes a ventas realizadas en la empresa en un día; se leen:
    código y cantidad. Cada vez que lea un par de datos nuevos se debe 
    actualizar el stock y si este no es suficiente para realizar la venta se 
    debe informar al usuario el stock disponible de ese producto. Una vez 
    finalizada la carga de datos se debe informar al usuario el stock final
    de cada producto.
"""

from random import randint
stock=[]
for i in range(10):
    stock.append(randint(1,1000))

ventas=[]
for i in range(16):
    codigo=int(input('codigo del producto:'))
    if codigo in range(10):
        print('en stock:',stock[codigo])
        cantidad=int(input('cantidad:'))
        if cantidad<=stock[codigo]:
            c=(codigo,cantidad)
            ventas.append(c)
            stock[codigo]=stock[codigo]-cantidad
        else:
            print('stock insuficiente')
    else:
        print('codigo inexistente')

print('stock actualizado')
for i in range(10):
    print('codigo:',i,'stock:',stock[i])