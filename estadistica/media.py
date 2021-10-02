# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 23:18:00 2021

@author: Asus
"""

import random 

def mediax(X): 
    return sum(X)/len(X)

def varianza(X): 
    mu = mediax(X)
    c = 0
    for x in X: 
        c += (x-mu)**2
    
    return c/len(X)


def desviacion(X):
    v = varianza(X) 
    desviacion = v**0.5

    return desviacion

if __name__ == '__main__':
    X = [random.randint(1,21) for i in range(20)]
    mu=mediax(X)     
    v = varianza(X)
    d = desviacion(X)
    print(X)
    print(f'La media es {mu}')
    print(f'La varianza es {v}')
    print(f'La desviación estándar es {d}')