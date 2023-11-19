# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 10:05:05 2022

@author: yamil
"""

def mcd(a,b):
    diva=[]
    divb=[]
    for i in range(1,a+1):
        if a%i==0:
            diva.append(i)
    for i in range(1,b+1):
        if b%i==0:
            divb.append(i)
    divb.sort(reverse=True)
    for i in divb:
        if i in diva:
            mcd=i
            break
    return(mcd)

print(mcd(10,8))