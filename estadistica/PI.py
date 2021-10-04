# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 21:46:46 2021

@author: Asus
"""

import random 
import math
from media import  desviacion,mediax
from matplotlib import pyplot as plt
import matplotlib.patches as patches


def aventar_agujas(num): 
    dentro_circulo = 0
    X = []
    Y= []
    for _ in  range(num): 
        x = random.random() * random.choice([-1,1]) # del -1 al 1
        y = random.random() * random.choice([-1,1])
        distancia_centro = math.sqrt(x**2 + y**2)
        X.append(x)
        Y.append(y)
        
        if distancia_centro <=1: 
            dentro_circulo +=1
     
    return ( (4*dentro_circulo)/num, X,Y )

def estimacion(num_agujas, n_intentos): 
    estimados=[]
    X = []
    Y = []
    for _ in range(n_intentos): 
        estimacion_pi,X,Y = aventar_agujas(num_agujas)
        estimados.append(estimacion_pi)
    plots(X,Y)     
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
             
def plots(x,y):
    fig, ax = plt.subplots()
    ax.add_patch(
     patches.Rectangle(
        (-1, -1),
        2,
        2,
        edgecolor = 'red',
        facecolor = 'green',
        fill=False      
     ) )
    draw_circle = plt.Circle((0,0), 1, fill=False,color='blue')
    ax.set_aspect(1)
    ax.add_artist(draw_circle)
    
    x_c = []
    y_c = []
    x_f = []
    y_f = []
    for i,j in zip(x,y):
        distancia_centro = math.sqrt(i**2 + j**2)
        if distancia_centro<=1:
            x_c.append(i)
            y_c.append(j)
        else:
            x_f.append(i)
            y_f.append(j)
        
    plt.scatter(x_c,y_c, color='blue')
    plt.scatter(x_f,y_f, color='red')
    plt.show()

if __name__ == '__main__':
    estimar_pi(0.01,1000)
    