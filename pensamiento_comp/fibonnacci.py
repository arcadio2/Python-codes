# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 00:40:03 2021

@author: Asus
"""

def run():
    n=int(input('Escribe el numero de serie de fibbo: '))
    res = fibonnacci(n)
    print(res)
    
def fibonnacci(n):
    if n>1:
        return fibonnacci(n-1) + fibonnacci(n-2)
    else:
        return 1
    
if __name__ == '__main__':
    run()