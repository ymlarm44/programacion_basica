# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

''' 10. Un usuario desea conocer cuánto le cuesta el combustible 
de cada viaje que realiza en su auto. Para ello anota el kilometraje que 
marca el odómetro justo antes de iniciar el viaje, y toma nota nuevamente 
justo al llegar a destino. Conoce además el consumo de nafta del vehículo en 
ruta (es decir, cuantos litros gasta en promedio por cada kilómetro recorrido)
, y el precio del litro de nafta. Escriba un algoritmo para calcular el costo 
de un viaje. ¿Cómo modificaría el algoritmo para considerar un % de descuento 
para los días en que hay promociones para clientes habituales en la 
estación de servicio?'''

kminicial=float(input('kilometraje inicial: '))
kmfinal=float(input('kilometraje final: '))
kmviaje=kmfinal-kminicial
consumo_nafta=0.09
precio_nafta=105
costo_viaje=kmviaje*consumo_nafta*precio_nafta
costo_viaje=round(costo_viaje,2)
descuento=float(input('existe un descuento de combustible? ingresar porcentaje: '))
costo_viaje_descuento=costo_viaje-(descuento*costo_viaje/100)
costo_viaje_descuento=round(costo_viaje_descuento,2)
print('el costo del viaje es:',costo_viaje,'pesos')
print('el costo de viaje con descuento es:',costo_viaje_descuento,'pesos')

