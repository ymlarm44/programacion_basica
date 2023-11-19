# -*- coding: utf-8 -*-
"""
Created on Fri May 27 16:35:18 2022

@author: alumno
"""

archivo=open('cantidad-consultas-medicas-ambulatorias(1).txt')
datos=[]
for i in archivo:
    (u_o_id,u_o,a_2013,a_2014,a_2015,a_2016,a_2017,a_2018)=i.split(',')
    datos.append([u_o_id,u_o,a_2013,a_2014,a_2015,a_2016,a_2017,a_2018])
archivo.close()

a_2013=[]
a_2014=[]
a_2015=[]
a_2016=[]
a_2017=[]
a_2018=[]
for i in range(1,len(datos)):
    datos[i][2]=int(datos[i][2])
    datos[i][3]=int(datos[i][3])
    datos[i][4]=int(datos[i][4])
    datos[i][5]=int(datos[i][5])
    datos[i][6]=int(datos[i][6])
    datos[i][7]=int(datos[i][7])
for i in range(1,len(datos)):
    a_2013.append(datos[i][2])
    a_2014.append(datos[i][3])
    a_2015.append(datos[i][4])
    a_2016.append(datos[i][5])
    a_2017.append(datos[i][6])
    a_2018.append(datos[i][7])

print('cantidad de consultas totales:')
print('2013:',sum(a_2013))
print('2014:',sum(a_2014))
print('2015:',sum(a_2015))
print('2016:',sum(a_2016))
print('2017:',sum(a_2017))
print('2018:',sum(a_2018))

print(' ')

for i in range(1,len(datos)):
    if datos[i][2]==max(a_2013):
        print('unidad operativa con mas consultas en 2013:',datos[i][1],'con',datos[i][2],'consultas')
    if datos[i][3]==max(a_2014):
        print('unidad operativa con mas consultas en 2014:',datos[i][1],'con',datos[i][3],'consultas')
    if datos[i][4]==max(a_2015):
        print('unidad operativa con mas consultas en 2015:',datos[i][1],'con',datos[i][4],'consultas')
    if datos[i][5]==max(a_2016):
        print('unidad operativa con mas consultas en 2016:',datos[i][1],'con',datos[i][5],'consultas')
    if datos[i][6]==max(a_2017):
        print('unidad operativa con mas consultas en 2017:',datos[i][1],'con',datos[i][6],'consultas')
    if datos[i][7]==max(a_2018):
        print('unidad operativa con mas consultas en 2018:',datos[i][1],'con',datos[i][7],'consultas')

print(' ')
print('unidades operativas con menos de 1000 consultas en 2013:')        
for i in range(1,len(datos)):
    if datos[i][2]<1000:
        print(datos[i][1])

print(' ')
print('unidades operativas con menos de 1000 consultas en 2014:')        
for i in range(1,len(datos)):
    if datos[i][3]<1000:
        print(datos[i][1])
        
print(' ')
print('unidades operativas con menos de 1000 consultas en 2015:')        
for i in range(1,len(datos)):
    if datos[i][4]<1000:
        print(datos[i][1])

print(' ')
print('unidades operativas con menos de 1000 consultas en 2016:')        
for i in range(1,len(datos)):
    if datos[i][5]<1000:
        print(datos[i][1])

print(' ')
print('unidades operativas con menos de 1000 consultas en 2017:')        
for i in range(1,len(datos)):
    if datos[i][6]<1000:
        print(datos[i][1])

print(' ')
print('unidades operativas con menos de 1000 consultas en 2018:')        
for i in range(1,len(datos)):
    if datos[i][7]<1000:
        print(datos[i][1])

top=[]
for i in range(1,len(datos)):
    suma=datos[i][2]+datos[i][3]+datos[i][4]+datos[i][5]+datos[i][6]+datos[i][7]
    top.append([datos[i][1],suma])

top_ord=sorted(top,key=lambda x:x[1],reverse=True)

top_10=[]

for i in range(10):
    top_10.append(top_ord[i])

archivo_salida=open('Top10Consultas.txt','w')
for i in range(10):
    archivo_salida.write(top_10[i][0]+','+str(top_10[i][1])+'\n')
archivo_salida.close()