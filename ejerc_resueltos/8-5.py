
# -*- coding: utf-8 -*-
"""
Created on Fri May 13 17:52:55 2022

@author: alumno
"""
c=12
f=10
matriz=[([0]*c)for i in range(f)]
print(matriz)

export=open('export.txt')
for i in export:
    pais,fecha,monto=(i.split(sep=' '))
    monto=int(monto.strip('\n'))
    pais=int(pais)
    mes=int(fecha[2:4])
    matriz[pais-1][mes-1]+=monto
export.close()
print(matriz)

for i in range(len(matriz)):
    print('total exportado al pais ',i+1,':',sum(matriz[i]))
mayor=0
pais=0
for i in range(len(matriz)):
    if matriz[i][2]>mayor:
        mayor=matriz[i][2]
        pais=i+1
print('el pais con mayor exportacion en marzo:',pais)