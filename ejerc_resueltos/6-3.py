# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 10:20:17 2022

@author: yamil
"""

def mcm(a,b):
    multia=[]
    multib=[]
    for i in range(1,(a*b)+1):
        multia.append(a*i)
        multib.append(b*i)
    for i in multia:
        if i in multib:
            mcm=i
            break
    return(mcm)

print(mcm(6,4))