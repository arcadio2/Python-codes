# -*- coding: utf-8 -*-
"""
Created on Sun Sep 26 21:14:12 2021

@author: Asus
"""

import random
from matplotlib import pyplot as plt
from media import mediax,desviacion


def tirar_dados(n_tiros): 
    secuencia_de_tiros = []
    for _ in range(n_tiros):
        tiros = []
        suma_tiros = 0
        #TEOREMA DE LIMITE CENTRAL tirando varios dados a la vez
        for i in range(1000): #tiramos N dados
            tiros.append(random.choice([1,2,3,4,5,6]))
            suma_tiros += tiros[i]
            
        #tiro = random.choice([1,2,3,4,5,6])
        #tiro2 = random.choice([1,2,3,4,5,6])
        #tiro_final = tiro+tiro2
        secuencia_de_tiros.append(suma_tiros)#"/len(tiros)"
    print(f'La media es: {mediax(secuencia_de_tiros)}')
    
    #plots(secuencia_de_tiros)
    return secuencia_de_tiros

def main(n_tiros, n_intentos):
    tiros = []
    for _ in range(n_intentos):
        secuencia = tirar_dados(n_tiros)
        #print("XD: ",secuencia)
        tiros.append(secuencia)

    tiros_con_1 = 0
    no_1 =0
    for tiro in tiros: 
        if 2 in tiro:
            tiros_con_1+=1
        else: 
            no_1+=1
    probabilidad_tiros_con_1 = tiros_con_1/n_intentos    
    print(f'La probabilidad de que salga 2 es {probabilidad_tiros_con_1}')
    probabilidad_sin_1 = no_1/n_intentos    
    print(f'La probabilidad de que no salga 2 es {probabilidad_sin_1}')
    
    
def plots(x):
    plt.hist(x)
    plt.show()

if __name__ == '__main__':
    numero_tiros = int(input('Cuantos tiros de dados: '))
    numero_de_intentos = int(input('Cuantas veces quieres correr la simulación '))
    main(numero_tiros, numero_de_intentos)