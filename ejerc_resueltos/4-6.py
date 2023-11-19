# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 16:31:19 2022

@author: alumno
"""

'''6. Escriba un programa que lea dos números naturales y obtenga
 el máximo común divisor (MCD) de los mismos.'''
 
n1=int(input('ingrese un numero:')) 
n2=int(input('ingrese un numero:'))

divn1=[]
divn2=[]

for i in range(1,n1+1):
    if n1%i==0:
        divn1.append(i)

for i in range(1,n2+1):
    if n2%i==0:
        divn2.append(i)

divn1.sort(reverse=True)
divn2.sort(reverse=True)
print('los divisores de',n1,'son',divn1)
print('los divisores de',n2,'son',divn2)

for i in divn1:
    if i in divn2:
        print('el MCD es',i)
        break