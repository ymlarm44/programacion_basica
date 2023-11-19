# -*- coding: utf-8 -*-
"""
Created on Fri May 13 16:34:33 2022

@author: alumno
"""

'''1. Lea el archivo personal.txt que contiene un listado con los nombres 
 y apellidos de los agentes de la Facultad de Ingeniería de la UNER, y
 muestre el contenido del mismo por consola'''

file=open('personal.txt')
data=file.read()
print(data)
