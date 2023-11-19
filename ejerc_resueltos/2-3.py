# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 11:06:38 2022

@author: yamil
"""

peso=float(input('ingrese su peso en kg: '))
altura=float(input('ingrese su altura es metros: '))

imc=peso/(altura**2)
imc=round(imc,2)
print('su imc es:',imc)

if imc<18.5:
    print('bajo peso')
    
elif imc<24.9:
    print('peso normal')
    
elif imc<29.9:
    print('sobrepeso')

elif imc<34.9:
    print('obesidad tipo 1')

elif imc<39.9:
    print('obesidad tipo 2')

elif imc<=40:
    print('obesidad tipo 3')


    