# 5. Diseñe e implemente un programa en Python que permita ingresar un valor 
# numérico correspondiente a una medida en pies y devuelva la cantidad
# equivalente en metros. Nota: 1 pie = 0,3048 metros.
medida_pies=float(input('medida en pies:'))
medida_metros=round((medida_pies*0.3048),2)
print('la medida equivale a ',medida_metros,' metros')