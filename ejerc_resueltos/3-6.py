# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 10:11:54 2022

@author: yamil
"""

''' 6. Escriba un programa en Python que informe los números primos 
menores que 100. '''

multiplos=0
numero=1

print('numeros primos menores a 100')
while numero<=100:
    
    for divisor in range(1,numero+1):
        if (numero%divisor)==0:
            multiplos=multiplos+1
        elif multiplos==3:
            break
        
    if multiplos==2:
        print(numero)
   
    multiplos=0
    numero=numero+1
    
print('fin')

    