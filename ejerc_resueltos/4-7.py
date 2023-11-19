# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 16:59:08 2022

@author: alumno
"""
from random import randint
import math as m
x=[]
y=[]
cont=0
for i in range(1000):
    x.append(randint(-50,100))
    y.append(randint(-10,25))
cx=int(input('ingrese una coordenada x:'))
cy=int(input('ingerese una coordenada y:'))
r=int(input('ingrese el radio:'))

for i in range(1000):
    dist=m.sqrt(pow(cx-x[i],2)+pow(cy-y[i],2))
    if dist<r:
        cont=cont+1
print('hay',cont,'puntos dentro de la circunferencia')