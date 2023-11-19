# -*- coding: utf-8 -*-
"""
Created on Fri May 20 17:39:00 2022

@author: alumno
"""
lista=[]
archivo=open('CP.csv')
for i in archivo:
    i=i.strip('\n')
    i=i.split(sep=',')
    lista.append(i)

for i in range(len(lista)):
    for j in range(4):
        lista[i][j]=int(lista[i][j])

lista_2=[]
for i in range(len(lista)):
    cpx=(433/2)*((lista[i][2]+lista[i][3]-lista[i][0]+lista[i][1])/(lista[i][0]+lista[i][1]+lista[i][2]+lista[i][3]))
    cpy=(238/2)*((lista[i][0]+lista[i][2]-lista[i][1]+lista[i][3])/(lista[i][0]+lista[i][1]+lista[i][2]+lista[i][3]))
    cpx=round(cpx,2)
    cpy=round(cpy,2)
    cpx=str(cpx)
    cpy=str(cpy)
    lista_2.append((cpx,cpy))

archivo_salida=open('desplazamientos.txt','w')
archivo_salida.write('cpx'+','+'cpy'+'\n')
for i in range(len(lista_2)):
    archivo_salida.write(lista_2[i][0]+','+lista_2[i][1]+'\n')
archivo_salida.close()