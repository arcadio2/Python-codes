# -*- coding: utf-8 -*-
"""
Created on Fri Aug 13 00:30:23 2021

@author: Asus
"""

def divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors

def run():
    while True:
        try:
            try:
                num = int(input('Ingresa un número: '))
            except  ValueError:
                print("Ingrese números solamente")
                #return False
            if num <= 0 :
                raise ValueError("Ingresa un numero valido")
            print("TERMINA")
            break
        except ValueError as ve:
            print(ve)
            #return False
 
        #print("Debes ingresar un entero positivo")
        
if __name__ == '__main__':
    run()