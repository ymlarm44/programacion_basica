# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 08:24:43 2022

@author: yamil
"""

def listprim(n):
    lista=[]
    numero=1
    multiplos=0
    while len(lista)<n:

        for val in range (1,numero+1):
           if numero%val==0:
               multiplos=multiplos+1    
           if multiplos==3:
               break
         
        if multiplos==2:
            lista.append(numero)
        multiplos=0 
        numero=numero+1
    return(lista)

n=int(input('ingrese cantidad de numeros primos a generar:'))
lista=listprim(n)
print(lista)