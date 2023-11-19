# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 10:17:28 2022

@author: yamil
"""
''' 1. Escriba un programa en Python donde el usuario ingrese un número
 natural positivo y muestre por consola todos los valores impares desde 1 
 hasta el número ingresado. '''


i=0
numero=int(input('ingrese un numero:'))
print('numeros impares hasta',numero)
while i<=numero:
    if i%2!=0:
        print(i)
    i+=1
print('fin')
