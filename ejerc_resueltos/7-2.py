# -*- coding: utf-8 -*-
"""
Created on Wed May  4 09:46:14 2022

@author: yamil
"""

frase=input('ingrese frase:')
letra=input('ingrese letra:')

frase=frase.lower()
c=frase.count(letra)
print('la letra aparece',c,'veces en la frase')