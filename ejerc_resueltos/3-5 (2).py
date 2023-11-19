# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 17:43:07 2022

@author: alumno
"""

numero=int(input('ingrese un numero entero:'))
multiplos=0

for val in range (1,numero+1):
   if numero%val==0:
       multiplos=multiplos+1
   if multiplos==3:
       break
   
if multiplos==2:
    print('el numero',numero,'es primo')

elif multiplos==3:
    print('el numero',numero,'no es primo')
    
    