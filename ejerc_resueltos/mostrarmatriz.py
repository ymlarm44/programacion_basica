# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 09:56:57 2022

@author: yamil
"""

def mostrarmatriz(m):
    for i in range(len(m)):
        print('[',end=" ")
        for j in range(len(m[i])):
            print("{:>7}".format(m[i][j]),end=" ")
        print(']')