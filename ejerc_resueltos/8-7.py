# -*- coding: utf-8 -*-
"""
Created on Tue May 31 15:02:06 2022

@author: yamil
"""
registro=[]
nombre=input('nombre:')
while nombre != '0':
    apellido=input('apellido:')
    edad=input('edad:')
    dni=input('dni:')
    peso=float(input('peso:'))
    altura=float(input('altura:'))
    imc=peso/(altura**2)
    imc=round(imc,2)
    if imc<18.5:
        cond_imc='bajo peso'
    elif imc<24.9:
        cond_imc='peso normal'
    elif imc<29.9:
        cond_imc='sobrepeso'
    elif imc<34.9:
        cond_imc='obesidad tipo 1'
    elif imc<39.9:
        cond_imc='obesidad tipo 2'
    elif imc<=40:
        cond_imc='obesidad tipo 3'    
    imc=str(imc)
    registro.append([nombre,apellido,edad,dni,peso,altura,imc,cond_imc])
    nombre=input('nombre:')

archivo_salida=open('registro_imc_ej8_7.txt','w')
for i in range(len(registro)):
    for j in range(8):
        archivo_salida.write(str(registro[i][j])+',')
    archivo_salida.write('\n')
archivo_salida.close()
