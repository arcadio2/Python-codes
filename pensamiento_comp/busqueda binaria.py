# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 23:03:51 2021

@author: Asus
"""

def run():
   objetivo=int(input('Escoge un número: '))
   epsilon=0.001 #es nuestro (error)
   bajo=0
   alto=objetivo
   respuesta = (alto+bajo)/2 #punto medio
   while abs(respuesta**2-objetivo) >= epsilon:
      # print(abs(respuesta**2-objetivo))
       if respuesta**2<objetivo:
           bajo = respuesta
       else:
           alto=respuesta
       respuesta = (alto+bajo)/2
   print(f'la raíz cuadrada de {objetivo} es {respuesta}')
   binaria()

def binaria():
    lista = [4,8,1,9,12,123,13,18,16,15,2,32,43,76]
    lista.sort()
    print(lista)
    objetivo=int(input('Escruba el objetivo: '))
    menor=0
    mayor=len(lista)
    medio = int(menor + (mayor-menor)/2)
    respuesta = 0
    #print(lista[medio])
    while menor<=mayor:
        if lista[medio]==objetivo:
            break
        if int(menor)+1>=int(mayor):
            medio=-1
            break
        if lista[medio]<objetivo:
            menor = medio
        else: 
            mayor=medio
        medio=int(menor + (mayor-menor)/2)
    if medio!=-1: 
        print(f'{medio }: {lista[medio]}')
    else: 
        print("No existe el objetivo en la lista")

if __name__ == '__main__':
    run()