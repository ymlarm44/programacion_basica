# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 17:47:06 2022

@author: alumno
"""

'''5. Se ingresan por pantalla los siguientes datos de un grupo de pacientes
 de un centro médico: Nombre, DNI, Sexo (M o F), Obra Social y edad. Si un
 paciente no tiene Obra Social se ingresa “---“. Determine e informe: 

a) El % de mujeres del grupo. 

b) El número de pacientes menores a 45 años. 

c) Muestre solo nombre y DNI de los pacientes cuya obra social 
    es IOSPER.
    '''

pacientes=[]

nombre=input('ingrese nombre:')
while nombre !='0':
    dni=int(input("Ingrese su DNI: "))
    sexo=input("Ingrese su sexo: ")
    os=input("Ingrese su obra social: ")
    edad=int(input("Ingrese su edad: "))
    p=(nombre,dni,sexo,os,edad)
    pacientes.append(p)
    nombre=input("Ingrese su nombre: ")

#a)
cant_f=0
for i in range(len(pacientes)):
    if pacientes[i][2]=='f':
        cant_f=cant_f+1
        
porc_muj=round((cant_f/len(pacientes)*100),1)
print('el porcentaje de mujeres:',porc_muj)

#b)
nm45=0
for i in range(len(pacientes)):
    if pacientes[i][4]<45:
        nm45=nm45+1
print('la cantidad de pacientes menores a 45 son:',nm45)

#c)
for i in range(len(pacientes)):
    if pacientes[i][3]=='iosper':
        print(pacientes[i][0],pacientes[i][1])
