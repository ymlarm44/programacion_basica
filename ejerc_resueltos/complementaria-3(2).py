# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 15:32:55 2022

@author: yamil
"""

registro=[]
for i in range(15):
    pais=input('pais:')
    infectados=int(input('numero infectados:'))
    fallecidos=int(input('numero fallecidos:'))
    x=(pais,infectados,fallecidos)
    registro.append(x)

#a)
mortalidad=0
for i in range(15):
    mortalidad=mortalidad+registro[i][2]

print('el porcentaje de mortalidad del pais 5 es:',round(((registro[4][2]/mortalidad)*100),2),'%')

#b)
mortalidad_sup3=[]
for i in range(15):
    porc_mortalidad=round(((registro[i][2]/mortalidad)*100),2)
    if porc_mortalidad>3:
        mortalidad_sup3.append(registro[i][0])
print('los',len(mortalidad_sup3),'paises con mortalidad superior al 3% son:',mortalidad_sup3)

#c)
print('el total de muertes en 2020:',mortalidad)