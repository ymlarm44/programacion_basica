# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

'''
numero=int(input('ingrese un numero:'))
if numero%2==0:
    print('el numero es par')
else:
    print('el numero es impar')
if numero%5==0 and numero%3==0:
    print('es multiplo de 5 y 3')
elif numero%3==0:
    print('es multiplo de 3')
elif numero%5==0:
    print('es multiplo de 5')
'''

print('''precios:
         menor de 4 años gratis
         entre 4 y 18 años $150
         mayor de 18 años $250''')
                  
edad=int(input('ingrese su edad:'))

if edad<4:
   print('la entrada es gratis')

elif 4<edad<18:
   print('la entrada cuesta $150')

else:
   print('la entrada cuesta $250')    