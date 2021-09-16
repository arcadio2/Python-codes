# -*- coding: utf-8 -*-
"""
Created on Fri Aug 13 21:41:03 2021

@author: Asus
"""


def divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors

def run():
    num =input('Ingresa un número: ')
    assert num.isnumeric() or int(num) >0, "Debes escribir un numero y mayor a 0"
                #return False
    print(divisors(int(num)))
    print("Terminó mi programa")
 
        #print("Debes ingresar un entero positivo")
        
if __name__ == '__main__':
    run()