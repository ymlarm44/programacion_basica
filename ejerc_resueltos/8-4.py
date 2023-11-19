# -*- coding: utf-8 -*-
"""
Created on Tue May 31 14:36:51 2022

@author: yamil
"""

'''
4. El archivo PALABRAS.TXT contiene una lista de 
palabras (una x línea) en singular. Reescriba 
el archivo pasando todas las palabras al plural, 
agregando “s” si termina en vocal o “es” si termina 
en consonante.
'''

archivo=open('PALABRAS.TXT')
palabras=[]
for i in archivo:
    i=i.strip('\n')
    palabras.append(i)
archivo.close()
vocales=['a','e','i','o','u']
palabras_cor=[]
for i in palabras:
    if (i[-1]).isalpha() and i[-1] in vocales:
        pal=i+'s'
        palabras_cor.append(pal)
    elif (i[-1]).isalpha():
        pal=i+'es'
        palabras_cor.append(pal)
print(palabras_cor)