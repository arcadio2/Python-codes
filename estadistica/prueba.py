# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 17:08:23 2021

@author: Asus
"""
import numpy as np
import statistics as stat

lista = [155,42,67,269,234,266,217,232,62,89,219,230,233,272,225,91,138,
         341,397,362,108,171,484,537,381,459,450,128,245,657,611,618,
         568,515,172,270,786,727]

print(f'Tamaño= {len(lista)}')

lista = sorted(lista)
print("----------------------DATOS ORDENADOS------------------------")
print(lista)
print("----------------------------------------------------------")
def repetidos(li, ls, lista):
    count = 0
    for i in range(li,ls):
        if(i in lista): 
            count+=1
    return count

count = repetidos(662,786,lista)

mean = np.mean(lista)
print(f'MEDIA = {mean}')

print(f'MEdiana = {lista[19]}')
moda=stat.mode(lista)
print(f'MODA = {moda}')
            
            