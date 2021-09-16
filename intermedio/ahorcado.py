# -*- coding: utf-8 -*-
"""
Created on Fri Aug 13 22:25:47 2021

@author: Asus
"""

import os
import functools
def obtenerLista():
    valores = []
    with open('./archivos/nombres.txt', "r",encoding="utf-8") as f:
        for line in f:
            valores.append(line.strip())
    return valores

def run():
    valores = obtenerLista()
    print(valores)
    os.system('cls')
    

if __name__ == '__main__':
    run()
