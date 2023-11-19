# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

pacientes=[]

nombre=input('nombre:')
while nombre !='0':
    dni=int(input('dni:'))
    sexo=input('sexo (m o f):')
    obra_social=input('obra social:')
    edad=int(input('edad:'))
    x=(nombre,dni,sexo,obra_social,edad)
    pacientes.append(x)
    nombre=input('nombre:')

#a)
n_mujeres=0
for i in range(len(pacientes)):
    if pacientes[i][2]=='f':
        n_mujeres=n_mujeres+1
porcentaje_mujeres=(n_mujeres/len(pacientes))*100
print('el porcentaje de mujeres en el grupo es:',porcentaje_mujeres,'%')

#b)
pacientes_men_45=0
for i in range(len(pacientes)):
    if pacientes[i][4]<45:
        pacientes_men_45=pacientes_men_45+1
print('cantidad de pacientes menores a 45:',pacientes_men_45)

#c)
print('pacientes con iosper:')
for i in range(len(pacientes)):
    if pacientes[i][3]=='iosper':
        print(pacientes[i][0],pacientes[i][1])
