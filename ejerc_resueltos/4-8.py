# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 17:23:10 2022

@author: alumno
"""

'''8. Leer el dni y las calificaciones (una calificación por alumno) 
de un grupo de alumnos que asistieron a una evaluación parcial de Fundamentos
 de Programación y almacenarlos en una lista. Los datos finalizan con el 
 dni 0. Se desea obtener como información de salida:'''
 
dni=[]
nota=[]

n=int(input('ingrese nota:'))
nota.append(n)
d=int(input('ingrese dni:'))
dni.append(d)

while d!=0:
    print('para finalizar ingrese 0:')
    n=int(input('ingrese nota:'))
    nota.append(n)
    d=int(input('ingrese dni:'))
    dni.append(d)
    
dni.pop()
nota.pop()

mayor_calif=0
dni_mayor_calif=0

print('los aprobados son:')
for i in range(len(dni)):
    if nota[i]>=60:
        print(dni[i])
    if mayor_calif<nota[i]:
        mayor_calif=nota[i]
        dni_mayor_calif=dni[i]
print('la mayor nota es',mayor_calif,'correspondiente a ',dni_mayor_calif)
