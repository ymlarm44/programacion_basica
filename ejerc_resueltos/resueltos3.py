# -*- coding: utf-8 -*-
"""
Created on Sun Jun  5 14:13:51 2022

@author: yamil
"""

archivo=open('DatosFlujoVehicular_20220223_AVE.csv')
datos=[]
for i in archivo:
    datos.append(i.split(';'))
archivo.close()
autos=[]
for i in range(6,30):
    autos.append((datos[i][1],datos[i][2]))

cant_aut_centro=0
cant_aut_prov=0
for i in range(len(autos)):
    cant_aut_centro+=int(autos[i][0])
    cant_aut_prov+=int(autos[i][1])

print('A)','centro:',cant_aut_centro,'provincia:',cant_aut_prov)

suma_filas=[]
for i in range(6,30):
    suma=0
    for j in range(1,9,2):
        suma+=int(datos[i][j])
    suma_filas.append(suma)
print('B) hora:',suma_filas.index(max(suma_filas)),'centro:',max(suma_filas))

suma_filas=[]
for i in range(6,30):
    suma=0
    for j in range(2,9,2):
        suma+=int(datos[i][j])
    suma_filas.append(suma)
print('   hora:',suma_filas.index(max(suma_filas)),'provincia:',max(suma_filas))