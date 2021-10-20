# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 21:36:58 2021

@author: Asus
"""

import time 
import sys

def factorial(n):
    if  n == 1:
        return 1
    return n * factorial(n-1)

def factorial_i(n):
    respuesta = 1
    while n>1: 
        respuesta *=n
        n-=1
    return respuesta

if __name__ == '__main__':
    n=9999
    sys.setrecursionlimit(n+100)
    comienzo = time.time()
    a=factorial(n)
    final = time.time()
    print("TIEMPO RECURSIVO ",(final-comienzo))
    comienzo = time.time()
    b = factorial_i(n)
    final = time.time()
    print("TIEMPO ITERATIVO ",(final-comienzo))