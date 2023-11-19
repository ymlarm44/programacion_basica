# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 19:42:41 2022

@author: yamil
"""
'''
1. En una olimpíada estudiantil compiten N alumnos en 3 pruebas
 (1: matemáticas, 2: física y 3: computación).
 Se ingresan por cada inscripto el DNI y su número asignado para la competencia
 (entre 1 y N). Luego, sin orden alguno, se van ingresando ternas con los 
 puntajes de cada prueba: nro de participante, código de actividad 
 (1: matemáticas, 2: física y 3: computación), puntaje en la actividad. 
  Escriba un algoritmo que determine:

a) El DNI del ganador de la competencia y el puntaje total obtenido.

b) El DNI del estudiante que ocupó el 2do lugar y su puntaje.

c) ¿Qué puntaje obtuvo en Computación el ganador de la competencia?

    '''

registro=[]
n=int(input('numero de competidores:'))

for i in range(n):
    dni=int(input('dni del competidor:'))
    prueba1=int(input('puntaje prueba 1:'))
    prueba2=int(input('puntaje prueba 2:'))
    prueba3=int(input('puntaje prueba 3:'))
    x=(i,dni,prueba1,prueba2,prueba3)
    registro.append(x)

puntajes=[]
for i in range(n):
    suma=registro[i][2]+registro[i][3]+registro[i][4]
    puntajes.append(suma)

#a)
for i in range(n):
    if puntajes[i]==max(puntajes):
        print('ganador:',registro[i][1],'puntaje:',puntajes[i])

#b)
puntaje_sp=0
dni_sp=0
for i in range(n):
    if puntajes[i]<max(puntajes) and puntajes[i]>puntaje_sp:
        puntaje_sp=puntajes[i]
        dni_sp=registro[i][1]
print('segundo puesto:',dni_sp,'puntaje:',puntaje_sp)
        
#c)
for i in range(n):
    if puntajes[i]==max(puntajes):
        print('el ganador obtuvo en computacion',registro[i][4],'como puntaje')    
