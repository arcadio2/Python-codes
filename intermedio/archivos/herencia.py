# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 21:42:48 2021

@author: Asus
"""

class Rectangulo: 
    
    def __init__(self, base, altura):
        self.base=base
        self.altura=altura
    
    def area(self):
        return self.base * self.altura

class Cuadrado(Rectangulo): 
    
    def __init__(self, lado): 
        super().__init__(lado, lado)
    



if __name__ == '__main__':
    rectangulo = Rectangulo(base=3,altura=4)
    print(rectangulo.area())
    cuadrado = Cuadrado(lado=4)
    print(cuadrado.area())