# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 10:29:41 2022

@author: yamil
"""

def es_par(n):
    if n%2==0:
        n=True
    else:
        n=False
    return(n)

def divisores(a):
    divisores=[]
    for i in range(1,a+1):
        if a%i==0:
            divisores.append(i)
    return(divisores)

def es_primo(a):
    if a==2:
        a=True
    for i in range(2,a):
        if a%i==0:
            a=False
        else:
            a=True
    return(a)

def factorial(n):
    factorial=1
    for i in range(1,n+1):
        factorial=factorial*i
    return(factorial)