# -*- coding: utf-8 -*-
"""
Created on Tue May 17 13:52:32 2022

@author: yamil
"""

'''Lea el archivo de texto Lista.txt y obtenga el promedio de cada estudiante.

Escriba otro archivo Condicion.txt que contenga en la primera línea el nombre
 del alumno y su promedio y en la segunda línea la condición del alumno.

La condición queda determinada según el promedio de las notas: entre 60 y 80, 
alumno regular, mayor a 80 promocional y libre en otro caso. '''

datos=open('lista.txt')
lista=[]
for i in datos:
    i=i.strip('\n')
    lista.append(i)
datos.close()

nombres=[]
for i in range(0,len(lista),2):
    nombres.append(lista[i])

notas=[]
for i in range(1,len(lista),2):
    notas.append(lista[i].split(sep=' '))

import statistics as s
promedios=[]
for i in range(len(notas)):
    notas[i][0]=int(notas[i][0])
    notas[i][1]=int(notas[i][1])
    notas[i][2]=int(notas[i][2])
    promedios.append(round((s.mean(notas[i])),1))

datos_salida=open('condicion.txt','w')
for i in range(len(nombres)):
    if promedios[i]>80:
        condicion='condicion: promocional'
    elif promedios[i]<80 and promedios[i]>60:
        condicion='condicion: regular'
    else:
        condicion='condicion: libre'
    datos_salida.write(nombres[i]+' '+'promedio: '+str(promedios[i])+'\n'+condicion+'\n')
datos_salida.close()
    