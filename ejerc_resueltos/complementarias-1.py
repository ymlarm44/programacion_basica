# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal
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


competidores=[]
dni=int(input('ingrese DNI:'))
while dni!=0:
    iden=int(input('ingrese ID:'))
    prueba1=int(input('ingrese puntaje en prueba 1:'))
    prueba2=int(input('ingrese puntaje en prueba 2:'))
    prueba3=int(input('ingrese puntaje en prueba 3:'))
    c=(iden,dni,prueba1,prueba2,prueba3)
    competidores.append(c)
    dni=int(input('ingrese DNI:'))

puntajes=[]
maxi=[]
for i in range(0,len(competidores)):
    puntaje=competidores[i][2]+competidores[i][3]+competidores[i][4]
    pun=(competidores[i][1],puntaje)
    puntajes.append(pun)
    maxi.append(puntaje)
        
segundo_puntaje=0
segundo_ganador=0
maxi.sort(reverse=True)
maximo=maxi[0]
for i in range(0,len(puntajes)):
    if puntajes[i][1]==maximo:
        ganador=i
        print('el ganador es:',puntajes[i][0],'con puntaje total:',puntajes[i][1])
    elif puntajes[i][1]<maximo and puntajes[i][1]>segundo_puntaje:
        segundo_puntaje=puntajes[i][1]
        segundo_ganador=puntajes[i][0]
print('el segundo lugar es:',segundo_ganador,'con puntaje total:',segundo_puntaje)       

print('el ganador de la competencia obtuvo en computacion un puntaje igual a:',competidores[ganador][4])


    