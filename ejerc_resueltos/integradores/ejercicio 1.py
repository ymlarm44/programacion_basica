# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

datos=[]
archivo=open('clinica.txt')
for i in archivo:
    codigo,servicio,fecha,visitas=i.split(',')
    visitas=int(visitas.strip('\n'))
    datos.append([codigo,servicio,fecha,visitas])
archivo.close()

clinica2020=[]
clinica2021=[]
clinica2022=open('clinica2022.txt','a')

for i in range(len(datos)):
    if datos[i][2][-1]=='0':
        clinica2020.append(datos[i])
    elif datos[i][2][-1]=='1':
        clinica2021.append(datos[i])
    else:
        clinica2022.write(datos[i][0]+','+datos[i][1]+','+datos[i][2]+','+str(datos[i][3])+'\n')
clinica2022.close()

clinica2022=[]
archivo2=open('clinica2022.txt')
for i in archivo2:
    codigo,servicio,fecha,visitas=i.split(',')
    visitas=int(visitas.strip('\n'))
    clinica2022.append([codigo,servicio,fecha,visitas])
archivo2.close()
    
clinica2020_salida=open('clinica2020.txt','w')
for i in range(len(clinica2020)):
    clinica2020_salida.write(clinica2020[i][0]+','+clinica2020[i][1]+','+clinica2020[i][2]+','+str(clinica2020[i][3])+'\n')
clinica2020_salida.close()

clinica2021_salida=open('clinica2021.txt','w')
for i in range(len(clinica2021)):
    clinica2021_salida.write(clinica2021[i][0]+','+clinica2021[i][1]+','+clinica2021[i][2]+','+str(clinica2021[i][3])+'\n')
clinica2021_salida.close()

año=input('ingrese año a consultar (2020/2021/2022):')
while año!='2020' and año!='2021' and año!='2022':
    print('ERROR! no se encuentran registros de ese año')
    año=input('ingrese año a consultar (2020/2021/2022):')
    
if año=='2020':
    archivo=clinica2020
elif año=='2021':
    archivo=clinica2021
elif año=='2022':
    archivo=clinica2022

#A)
print(' ')
lista=[]
for i in range(len(archivo)):
    if [archivo[i][1],0] not in lista:
        lista.append([archivo[i][1],0])

for i in range(len(archivo)):
    for j in range(len(lista)):
        if archivo[i][1]==lista[j][0]:
            lista[j][1]+=archivo[i][3]

from operator import itemgetter
top5serv=[]
lista_ord=sorted(lista,key=itemgetter(1),reverse=True)
for i in range(5):
    top5serv.append(lista_ord[i])
print('los 5 servicios mas consultados:',top5serv)

#B)
print(' ')
lista2=[]
for i in range(len(archivo)):
    if [archivo[i][2][3]+archivo[i][2][4],0] not in lista2:
        lista2.append([archivo[i][2][3]+archivo[i][2][4],0])
for i in range(len(archivo)):
    for j in range(len(lista2)):
        if archivo[i][2][3]+archivo[i][2][4]==lista2[j][0]:
            lista2[j][1]+=archivo[i][3]
lista2_ord=sorted(lista2,key=itemgetter(1),reverse=True)
print('el mes que mas visitas tuvo:',lista2_ord[0])

#C)
print(' ')
lista3=[['verano',0],['invierno',0]]
for i in range(len(lista2)):
    if lista2[i][0]>='01' and lista2[i][0]<='03':
        lista3[0][1]+=lista2[i][1]
    elif lista2[i][0]>='07' and lista2[i][0]<='09':
        lista3[1][1]+=lista2[i][1]
print('numero de pacientes que visitaron la clinica en:',lista3)

#D)
print(' ')
import statistics as s
pediatria_julio=[]
for i in range(len(archivo)):
    dia,mes,anio=archivo[i][2].split('/')
    if archivo[i][1]=='Pediatría' and mes=='06':
        pediatria_julio.append(archivo[i][3])
print('el promedio de consultas para pediatria en julio:',s.mean(pediatria_julio))

#E)
print(' ')
servicios_ver=[]
for i in range(len(archivo)):
    dia,mes,anio=archivo[i][2].split('/')
    if mes>='12' or mes<='03':
        servicios_ver.append(archivo[i])
lista4=[] 
for i in range(len(archivo)):
    if [archivo[i][1],0] not in lista4:
        lista4.append([archivo[i][1],0])
for i in range(len(archivo)):
    for j in range(len(lista4)):
        if archivo[i][1]==lista4[j][0]:
            lista4[j][1]+=archivo[i][3]
top2serv_ver=[]
lista4_ord=sorted(lista4,key=itemgetter(1),reverse=True)
for i in range(2):
    top2serv_ver.append(lista4_ord[i])
print('los 2 servicios mas consultados en verano:',top2serv_ver)

#F)
print(' ')
suma=0
for i in range(len(archivo)):
    suma+=archivo[i][3]
print('cantidad de consultas en el año:',suma)