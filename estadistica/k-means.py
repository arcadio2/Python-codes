# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 16:09:54 2021

@author: Asus
"""

from matplotlib import pyplot as plt
import numpy as np
import pandas as  pd 
import matplotlib.patches as patches
import random 

def generate_random_vectors():
    vectors = []
    
    """
                                      #coords  #range x # range y  #TAM
    a = np.random.multivariate_normal([10,0], [[3,1], [1,4]], size=[10,])
    b = np.random.multivariate_normal([0,20], [[3,1], [1,4]], size=[10,])
    for i in range(10): 
        vector = (a[i][0],a[i][1])
        vectors.append(vector)
        vector2 = (b[i][0],b[i][1])
        vectors.append(vector2)
        random_vectors = []
    """
    for i in range(100):
        vectors.append((random.uniform(0, 25), random.uniform(0, 25)))
     
        
        
    return vectors
    

def distancia_euclidiana(d1,d2):
    x0=d1[0]
    x1=d2[0]
    y0=d1[1]
    y1=d2[1]
    return ((x1-x0)**2+(y1-y0)**2)**0.5

def plot(vector, color="red"):
    x=[]
    y=[]
    for coord in vector: 
        #print(coord)
        x.append(coord[0])
        y.append(coord[1])
    plt.scatter(x,y,color=color)
    #plt.show()

def puntos(punto, vectors): 
    vector_final = []
    for vector in vectors: 
        distancia = distancia_euclidiana(punto,vector)
        vector_final.append(distancia)     
    return vector_final

def matriz_distancias(vectors):
    index = 0
    matriz = []

    for vector in vectors: 
        vectores_obtenidos = puntos(vector, vectors)
        #print(vectores_obtenidos)
        index += 1
        matriz.append(vectores_obtenidos)
    data_df = pd.DataFrame(matriz)
    return data_df
    #print(matriz)
def punto_mas_cercano(coord,vector):
    cercano = 10000
    aux = (0,0)
    for i in vector:
        d = distancia_euclidiana(coord,i)
        if d !=0:
            if cercano>d: 
                cercano = d
                aux = i
                
    return aux


def vector_con_removidos(vector,coord,coord2): 
    vector_final = []
    for j in vector:
        if coord != j and coord2 != j:
            vector_final.append(j)
    
    
    return vector_final

def k_aleatorios(k):
    lista = []
    for i in range(k): 
        x = random.randint(-4, 14)
        y = random.randint(-5, 25)
        coords = (x,y)
        lista.append(coords)
    return lista

def k_definidos(vectores):
    x=[]
    y=[]
    for vector in vectores:
        x.append(vector[0])
        y.append(vector[1])
    mean_x = np.mean(x)
    mean_y= np.mean(y)
    return (mean_x,mean_y)

def obtener_k(matriz):
    lista = []
    for vector in matriz: 
        punto = k_definidos(vector)
        lista.append(punto)
        
    return lista

def vectores_agrupados(vectores, kas):
    matriz = []
    lista = []
    for k in kas: 
        matriz.append([])
    
    for vector in vectores: 
        dis_min = 1000 
        k_aux = (0,0)
        for k in kas:
            d = distancia_euclidiana(k,vector)
            if dis_min>d:
                dis_min = d            
                k_aux = k
        lista.append({k_aux:vector})
    for l in lista: 
        index = 0
        for k in kas: 
            if l.get(k): 
                matriz[index].append(l.get(k))
            index+=1
    for m in matriz: 
        if len(m)==0: 
            m.append((0,0))
            
    return matriz 

def vectores_iguales(matriz_anterior, matriz):
    index = 0
    bandera = False
    for m in matriz: 
        if m != matriz_anterior[index]:
            bandera = True
        else: 
            bandera = False
        index +=1
    return bandera
    
    
def plots_con_k(p_c, c_c, kas, matriz): 
    index = 0
    for i in kas:
        plt.scatter(i[0],i[1], color=c_c[index], s=100)
        if(len(matriz[index]) !=0):
            plot(matriz[index], color = p_c[index])
        index+=1   
    plt.show()       
    
if __name__ == '__main__':
    POINTS_COLOURS = ['turquoise', 'lime', 'dodgerblue', 'fuchsia', 'lightcoral', 'navajowhite']
    CLUSTERS_COLOURS = ['teal', 'green', 'blue', 'purple', 'red', 'goldenrod']
    vectors = generate_random_vectors()
    plot(vectors)

    K = 4 # GRUPOS MAXIMO 6 por los colores
    kas = k_aleatorios(K)
    index = 0
    for i in kas:
        plt.scatter(i[0],i[1], color=CLUSTERS_COLOURS[index])
        index+=1
    plt.show()


    nuevos_k = kas
    matriz = vectores_agrupados(vectors,nuevos_k)
    index = 0
    plots_con_k(POINTS_COLOURS, CLUSTERS_COLOURS,nuevos_k,matriz)
    
    matriz_anterior=[]
    for n in range(K):
        matriz_anterior.append([])
    
    
    while vectores_iguales(matriz_anterior, matriz): 
        matriz_anterior = matriz
        nuevos_k=obtener_k(matriz) 
        matriz = vectores_agrupados(vectors,nuevos_k)
        plots_con_k(POINTS_COLOURS, CLUSTERS_COLOURS,nuevos_k,matriz)
    "ULTIMO PASO POR SI HAY UNA PEQUEÑA DIFERENCIA"
    nuevos_k=obtener_k(matriz) 
    matriz = vectores_agrupados(vectors,nuevos_k)
    index = 0

    plots_con_k(POINTS_COLOURS, CLUSTERS_COLOURS,nuevos_k,matriz)
   
