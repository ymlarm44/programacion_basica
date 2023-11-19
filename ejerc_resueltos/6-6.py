# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 09:53:44 2022

@author: yamil
"""
from random import randint
import mostrarmatriz as mm

#a)
registro=[('paciente','dia 1','dia 2','dia 3','dia 4','dia 5','dia 6','dia 7')]

for i in range(1,66):
    n=i
    d1=randint(70,100)
    d2=randint(70,100)
    d3=randint(70,100)
    d4=randint(70,100)
    d5=randint(70,100)
    d6=randint(70,100)
    d7=randint(70,100)
    registro.append((n,d1,d2,d3,d4,d5,d6,d7))
    
mm.mostrarmatriz(registro)

#b)
def hipox(lista):
    resultado=0
    for i in range(1,len(lista)):
        for j in range(1,7):
            if lista[i][j]<72 and lista[i][j+1]<72:
                resultado=resultado+1
    return(resultado)

np_hipoxemia=hipox(registro)
print('cantidad de pacientes con hipoxemia:',np_hipoxemia)