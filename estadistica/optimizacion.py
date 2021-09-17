# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 14:20:47 2021

@author: Asus
"""

def fibonacci_recursivo(n):
    if n == 0 or n==1:
        return 1
    
    return fibonacci_recursivo(n-1) + fibonacci_recursivo(n-2)

def fibonacci_dinamico(n, memo = {}):
    if n == 0 or n==1:
        return 1
    try:
        return memo[n]
    except KeyError: 
        resultado = fibonacci_dinamico(n-1, memo) + fibonacci_dinamico(n-2, memo)
        memo[n]  = resultado 
        print(memo)
        return resultado

if __name__ == '__main__':
    n= int(input("ESCOGE UN NÚMERO: "))
    resultado = fibonacci_dinamico(n)
    print(resultado)