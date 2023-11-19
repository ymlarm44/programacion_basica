# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 16:56:10 2022

@author: alumno
"""
from random import randint

base=('A','C','T','G')
lista=[]
for i in range(5000):
    rand=randint(0,3)
    lista.append(base[rand])

print(lista)

#a)
A=lista.count('A')
C=lista.count('C')
T=lista.count('T')
G=lista.count('G')

total=A+C+T+G

prop_A=(A/total)*100
prop_C=round((C/total)*100,2)
prop_T=(T/total)*100
prop_G=round((G/total)*100,2)

print('la proporcion de A es:',prop_A,)
print('la proporcion de C es:',prop_C,)
print('la proporcion de T es:',prop_T,)
print('la proporcion de G es:',prop_G,)

#b)
print('la cantidad total de nucleotidos T es:',T)

#c)
sec_CG=0
for i in range(len(lista)):
    if lista[i]=='C' and lista[i+1]=='G':
        sec_CG=sec_CG+1
print('la cantidad de veces que aparece la secuencia CG es:',sec_CG)
