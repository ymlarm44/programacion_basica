# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 09:57:57 2022

@author: yamil
"""
def mostrarmatriz(m):
    for i in range(len(m)):
        print('[',end=" ")
        for j in range(len(m[i])):
            print("{:>5}".format(m[i][j]),end=" ")
        print(']')
registro=[]
from random import randint
for i in range(16):
    registro.append([])
    for c in range(9):
        registro[i].append(randint(0,1000))
mostrarmatriz(registro)

#a)
casos_mayo=0
for i in range(16):
    casos_mayo=registro[i][2]+casos_mayo
porc_dpto5_mayo=round((registro[4][2]/casos_mayo)*100,1)
print('a) el porcentaje de casos del departamento 5 sobre el total en el mes de mayo es:',porc_dpto5_mayo,'%')

#b)
minimo_julio=1000
dpto_minimo_julio=0
for i in range(16):
    if minimo_julio>registro[i][4]:
        minimo_julio=registro[i][4]
        dpto_minimo_julio=i+1
print('b) la menor cantidad de casos en julio se dio en el dpto',dpto_minimo_julio,'con',minimo_julio,'casos')

#c)
porc_junio=round(((registro[10][3]-registro[10][2])/registro[10][2])*100,2)
if porc_junio>0:
    print('c) en el dpto 11 el porcentaje de aumento entre mayo-junio fue de:',porc_junio,'%')
else:
    print('c) no hubo porcentaje de aumento entre mayo-junio en el dpto 11, sino un declive del',porc_junio,'% de casos con respecto a mayo')

