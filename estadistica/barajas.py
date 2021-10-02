# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 18:27:49 2021

@author: Asus
"""
import random
import collections
PALOS = ["espada", "corazón", "rombo", "trebol"]
VALORES = ["as","2","3","4","5","6","7","8","9","10","jota","reina","rey"]


def crear_baraja(): 
    barajas=[]
    for palo in PALOS: 
        for valor in VALORES: 
            barajas.append((palo,valor))
            
    return barajas


def obtener_mano(barajas,tamano_mano): 
    mano = random.sample(barajas,tamano_mano)
    return mano


def main(tam,intentos):
    barajas = crear_baraja()
    
    manos = []
    for _ in range(intentos):
        mano = obtener_mano(barajas,tam)
        manos.append(mano)
        
    pares = 0
    for mano in manos: 
        valores = []
        for carta in mano:
            valores.append(carta[1])

        counter = dict(collections.Counter(valores)) #NOs da la cantidad encontrada
        for valor in counter.values(): #values pq es un diccionario
            if valor == 2: 
                pares+=1
                break
    probabilidad_par = pares/intentos
    print(f'la probabilidad de obtener un par en una mano de tamaño {tam} es: {probabilidad_par}')
        
if __name__ == '__main__':
    tamano_mano = int(input('De cuantas barajas será la mano: '))
    intentos = int(input('Cuantos intentos quieres hacer: '))
    main(tamano_mano,intentos)