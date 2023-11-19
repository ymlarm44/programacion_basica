# -*- coding: utf-8 -*-
"""
Created on Fri May 13 17:12:13 2022

@author: alumno
"""

'''3. El archivo ECG.txt contiene 10000 valores registrados por un cardiólogo 
mediante un electrocardiograma. Lea el archivo ECG.txt y obtenga el promedio 
de los datos y cuántos valores superan un umbral (umbral = 20 * promedio).'''
registro=[]
data=open('ECG.txt')
for i in data:
    dato=i.strip('\n')
    dato=int(dato)
    registro.append(dato)
data.close()

import statistics as s
promedio=s.mean(registro)
print('promedio:',promedio)
umbral=20*promedio
c=0
for i in registro:
    if i>umbral:
        c=c+1
print('superan el umbral:',c)