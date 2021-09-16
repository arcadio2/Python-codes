# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 13:43:07 2021

@author: Asus
"""

class Coordenada:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def distancia(self,otra_coordenada):
        x_diff = (self.x-otra_coordenada.x)**2
        y_diff = (self.y-otra_coordenada.y)**2
        return(x_diff+ y_diff)**0.5
    

if __name__ == '__main__':
        cord_1 = Coordenada(3,30)
        coord_2 = Coordenada(4,8)
        x=1
        print(coord_2.distancia(cord_1))
        print(isinstance({},Coordenada))