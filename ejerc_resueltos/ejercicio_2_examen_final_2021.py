# -*- coding: utf-8 -*-
"""
Created on Mon May 23 21:33:36 2022

@author: yamil
"""
'''
Examen FuPro. 30/07/2020. Ejercicio 2.
Escriba un programa C++ que lea las temperaturas máximas diarias obtenidas en una región, a lo largo de un período de casi un año. 
Estas temperaturas están almacenadas en un archivo de texto TEMP.CSV con un dato por línea.  
Entre los valores registrados en la secuencia se hallan algunos datos ficticios expresados con 999.9, 
lo cual significa que por problemas en el sensor no se pudo obtener la temperatura máxima de ese día. 
El programa debe realizar lo sigu
'''


listatemp=[]
archi=open("temp.csv","r")
todo=archi.readlines()
for linea in todo:
     linea=linea.rstrip("\n")
     temp=int(linea)
     listatemp.append(temp)        

for i in range(1,len(listatemp)-1):
     if listatemp[i]==999:
            listatemp[i]=(listatemp[i-1]+listatemp[i+1])/2.0

if listatemp[0]==999:
      listatemp[0]=listatemp[1]

if listatemp[-1]==999:
      listatemp[-1]=listatemp[-2]                 

print(listatemp)