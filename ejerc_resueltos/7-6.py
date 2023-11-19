# -*- coding: utf-8 -*-
"""
Created on Fri May  6 16:57:15 2022

@author: yamil
"""

secuencia='ATGCAAATTGTGTGTGCATAATTTATATAGGCTAGAATAGAATCGCTA'
c=0
for i in secuencia:
    if i=='G' or i=='C':
        c=c+1
    
porcentaje_gc=(c/len(secuencia))*100

print('porcentaje de G Y C en ADN:',porcentaje_gc,'%')