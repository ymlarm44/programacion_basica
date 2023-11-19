# -*- coding: utf-8 -*-
"""
Created on Fri May  6 16:35:15 2022

@author: yamil
"""

nombre=input('ingrese nombre:')
apellido=input('ingrese apellido:')
institucion=input('ingrese institucion:')

email=nombre[0]+apellido+'@'+institucion+'.com'
email=email.lower()
print(email)