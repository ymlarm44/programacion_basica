# -*- coding: utf-8 -*-
"""
Created on Fri May 13 16:53:28 2022

@author: alumno
"""

'''2. Con la información obtenida en el ejercicio anterior escribir un archivo,
 correos.txt, con las direcciones de correo electrónico de los agentes.
 Este correo se forma con la primera letra del nombre seguido del apellido y 
 el dominio "@ingenieria.edu.ar"'''
correos=[]
file=open('personal.txt')
for i in file:
    i=i.lower()
    nombre,apellido=i.split(sep=' ')
    apellido=apellido.strip('\n')
    correos.append(nombre[0]+apellido+'@ingenieria.edu.ar')
file.close()

file2=open('correos.txt','w')
for i in correos:
    file2.write(i+'\n')
file2.close()