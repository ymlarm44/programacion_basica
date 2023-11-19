# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 18:08:22 2022

@author: yamil
"""

n=int(input('ingrese n numeros para serie fibonacci:'))
serie=[0,1]
for i in range(n):
        a=serie[i]+serie[i+1]
        serie.append(a)
serie.pop()
serie.pop()

archivo_salida=open('serie_fibonacci.txt','w')
for i in range(len(serie)):
    archivo_salida.write(str(serie[i]))
    if i<n-1:
        archivo_salida.write(',')
archivo_salida.close()