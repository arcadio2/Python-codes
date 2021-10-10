# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 12:46:20 2021

@author: Asus
"""

from matplotlib import pyplot as plt
import numpy as np
import pandas as  pd 
def generate_random_vectors():
    vectors = []
   # for _ in range(100):
                                     #coords #disp x  #disp y   #size
    a = np.random.multivariate_normal([10,0], [[3,1], [1,4]], size=[10,])
    b = np.random.multivariate_normal([0,20], [[3,1], [1,4]], size=[10,])
    for i in range(10): 
        vector = (a[i][0],a[i][1])
        vectors.append(vector)
        vector2 = (b[i][0],b[i][1])
        vectors.append(vector2)
    #vector = (a,b)
    #vectors.append(vector)
    return vectors
    

def distancia_euclidiana(d1,d2):
    x0=d1[0]
    x1=d2[0]
    y0=d1[1]
    y1=d2[1]
    return ((x1-x0)**2+(y1-y0)**2)**0.5

def plot(vector):
    x=[]
    y=[]
    for coord in vector: 
        #print(coord)
        x.append(coord[0])
        y.append(coord[1])
    plt.scatter(x,y,color="red")
    plt.show()

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



def cluster(vector):
    index = 0
    lista_final = []
    vector_aux = []
    listax = []

    for i in vector: 
        if(len(lista_final)==0):
            coord = i
            coord2 = punto_mas_cercano(coord, vector)
            vector_aux = vector_con_removidos(vector, coord, coord2)
            listax.append(coord)
            listax.append(coord2)
            lista_final.append(listax[:index+2])
        else: 
            coord = coord2
            coord2 = punto_mas_cercano(coord, vector_aux)
            listax.append(coord2)
            lista_final.append(listax[:index+2])
            
            vector_aux = vector_con_removidos(vector_aux, coord, coord2)
        index +=1
    
    return lista_final
   
    

if __name__ == '__main__':
    vectors = generate_random_vectors()
    plot(vectors)
    matriz = matriz_distancias(vectors)
    vector = matriz[0]
    #p=punto_mas_cercano(vectors[0],vectors)
    lista_final = cluster(vectors)
    lista_final.pop()
    
    for lista in lista_final:
        x=[]
        y=[]
        for l in lista: 
            x.append(l[0])
            y.append(l[1])
        draw_circle = plt.Circle((0, 0), 10,fill=False)
        #axes.set_aspect(1)
        #figure, axes = plt.subplots()
        #axes.add_artist(draw_circle)
        plt.scatter(x,y)
        
        plt.show()

    
    dataframe = pd.DataFrame(lista_final)
    

    