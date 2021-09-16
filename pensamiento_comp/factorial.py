# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 23:01:28 2021

@author: Asus
"""

def main():
    fac=int(input('Que factorial quiere sacar: '))
    res = 1
    xd=factorial(fac,1,res)
    print(xd)
    factoria = otrofactorial(fac)
    print(factoria)
def factorial(n,paso, fact):
    if paso<=n:
        fact = fact*paso
        paso=paso+1
        return factorial(n,paso,fact)
    else:
        return fact
    
def otrofactorial(n):
    if n == 1:
        return 1
    return n * otrofactorial(n-1)




if __name__ == '__main__':
    main()