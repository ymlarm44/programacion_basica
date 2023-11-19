# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 17:32:43 2022

@author: alumno
"""

registro=[]
nombre=input('nombre:')
while nombre!='0':
    parcial1=int(input('nota parcial 1:'))
    parcial2=int(input('nota parcial 2:'))
    tp=int(input('cantidad de tp aprobados:'))
    registro.append((nombre,parcial1,parcial2,tp))
    nombre=input('nombre:')

def condicion(registro):
    regulares=[]
    libres=[]
    for i in range(len(registro)):
        promedio=round((registro[i][1]+registro[i][2])/2,1)
        if promedio>60 and registro[i][3]>=5:
            regulares.append(registro[i][0])
        else:
            libres.append(registro[i][0])
    return regulares,libres

regulares,libres=condicion(registro)

print('condicion regular:',regulares)
print('condicion libre:',libres)