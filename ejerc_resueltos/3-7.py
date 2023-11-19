# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 18:09:36 2022

@author: alumno
"""

numero=1
multiplos=0
c=1

while c<=100:

    for val in range (1,numero+1):
       if numero%val==0:
           multiplos=multiplos+1
           
       if multiplos==3:
           break
     
    if multiplos==2:
        print('el valor ',c,'es:',numero)
        c=c+1
    multiplos=0
    
    numero=numero+1
