# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 16:30:59 2022

@author: alumno
"""
from random import uniform
registro=[]
for i in range(1990,1999):
    año=i
    t1=round(uniform(20,36),1)
    t2=round(uniform(20,36),1)
    t3=round(uniform(15,33),1)
    t4=round(uniform(10,30),1)
    t5=round(uniform(8,27),1)
    t6=round(uniform(5,24),1)
    t7=round(uniform(2,22),1)
    t8=round(uniform(0,20),1)
    t9=round(uniform(4,22),1)
    t10=round(uniform(10,30),1)
    t11=round(uniform(15,33),1)
    t12=round(uniform(20,36),1)
    registro.append((año,t1,t2,t3,t4,t5,t6,t7,t8,t9,t10,t11,t12))

print(registro)

#a)
def mayor(registro):
    mayor=0
    año=0
    for i in range(len(registro)):
        if registro[i][2]>mayor:
            mayor=registro[i][2]
            año=registro[i][0]
    return(mayor,año)

mayor,año=mayor(registro)
print('la mayor temperatura en febrero fue:',mayor,'en',año)

#b)
def dif_porcentual(a,b):
    resultado=round(((b-a)/a)*100,2)
    return(resultado)

b=dif_porcentual(registro[5][1],registro[6][7])
print('la diferencia porcentual es:',b)

#c)
temp=[]
for i in range(1,13):
    temp.append(registro[1][i])
temp.sort(reverse=True)
sumatoria=0
for i in range(1,7):
    sumatoria=sumatoria+registro[1][i]
promedio=round((sumatoria/6),1)
print('el promedio de las 6 temperaturas maximas de 1991 es:',promedio)