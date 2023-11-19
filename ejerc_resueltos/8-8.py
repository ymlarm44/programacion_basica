# -*- coding: utf-8 -*-
"""
Created on Fri May 20 16:34:37 2022

@author: alumno
"""

archivo=open('covid.csv')
lista=[]
for i in archivo:
    i=i.strip('\n')
    i=i.split(sep=',')
    lista.append([i[0],i[4]])
archivo.close()
print(lista)

registro=[]
for i in range(1,len(lista)):
    registro.append([lista[i][0],int(lista[i][1])])

from operator import itemgetter

registro_ord=sorted(registro,key=itemgetter(1),reverse=True)

for i in range(len(registro_ord)):
    registro_ord[i][1]=str(registro_ord[i][1])

#archivo_salida=open('Ranking5Covid.txt','w')
#archivo_salida.write('paises'+','+'casos activos'+'\n')
#for i in range(5):
#    archivo_salida.write(registro_ord[i][0]+','+registro_ord[i][1]+'\n')
#archivo_salida.close()



    