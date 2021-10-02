# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 21:46:46 2021

@author: Asus
"""

import random 
import math
from media import  desviacion,mediax


def aventar_agujas(num): 
    dentro_circulo = 0
    for _ in  range(num): 
        x = random.random() * random.choice([-1,1]) # del -1 al 1
        y = random.random() * random.choice([-1,1])
        distancia_centro = math.sqrt(x**2 + y**2)
        
        if distancia_centro <=1: 
            dentro_circulo +=1
            
    return (4*dentro_circulo)/num

def estimacion(num_agujas, n_intentos): 
    estimados=[]
    for _ in range(n_intentos): 
        estimacion_pi = aventar_agujas(num_agujas)
        estimados.append(estimacion_pi)
    media_estimada = mediax(estimados)
    sigma = desviacion(estimados)
    print(f'PI={round(media_estimada, 5)}, sigma = {round(sigma, 5)}')
    
    return (media_estimada,sigma)
    
def estimar_pi(precision, n_intentos): 
    num = 1000
    sigma = precision
    while sigma >= precision/1.96: #IC95%=(-1.96,1.96)
        media, sigma = estimacion(num, n_intentos)
        num *= 2
        
    return media
             
if __name__ == '__main__':
    estimar_pi(0.01,1000)
    