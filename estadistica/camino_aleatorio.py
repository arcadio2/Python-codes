# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 23:08:52 2021

@author: Asus
"""

from borracho import BorrachoTradicional
from campo import Campo
from coordenadas import Coordenada
from bokeh.plotting import  figure, show


def caminata(campo, borracho,pasos):
    inicio = campo.obtener_coordenada(borracho)
    
    for _ in range(pasos):
        campo.mover(borracho)
    return inicio.distance(campo.obtener_coordenada(borracho))
    
def simular_caminata(pasos, n_intentos,tipo_de_borracho):
    borracho = tipo_de_borracho(nombre='Arcadio')
    origen = Coordenada(0,0)
    distancias = []
    
    for _ in range(n_intentos):
        campo = Campo()
        campo.añadir(borracho,origen)
        simulacion = caminata(campo,borracho,pasos)
        distancias.append(round(simulacion,1))
    return distancias

def graficar(x,y):
    grafica = figure(title="Camino aleatorio", x_axis_label='pasos', 
                     y_axis_label="ditancia")
    grafica.line(x,y,legend='Distancia media')
    
    show(grafica)
    

def main(distancias_de_caminata, n_intentos, BorrachoTradicional):
    distancias_medias = []
    for pasos in distancias_de_caminata:
        #10,100,1000,10000
        distancias = simular_caminata(pasos, n_intentos,BorrachoTradicional)
        distancia_media = round(sum(distancias)/len(distancias),4)
        distancia_maxima = max(distancias)
        distancia_minima = min(distancias)
        distancias_medias.append(distancia_media)
        print(f'{BorrachoTradicional.__name__} caminata aleatoria de  {pasos}')
        print(f'Media = {distancia_media}')
        print(f'Max = {distancia_maxima}')
        print(f'Min = {distancia_minima}')
    graficar(distancias_de_caminata,distancias_medias)

if __name__ == '__main__':
    distancias_de_caminata = [10,100,1000,10000]
    n_intentos = 100
    
    main(distancias_de_caminata, n_intentos, BorrachoTradicional)