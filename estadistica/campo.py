# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 22:59:28 2021

@author: Asus
"""

class Campo: 
    def __init__(self):
         self.coordnadas_borrachos = {}
         
    def añadir(self,borracho, coordenada):
        self.coordnadas_borrachos[borracho] = coordenada
        
    def mover(self, borracho):
        delta_x, delta_y = borracho.camina()
        coordenada_acutal = self.coordnadas_borrachos[borracho]
        nueva_coordenada =  coordenada_acutal.mover(delta_x, delta_y)
        self.coordnadas_borrachos[borracho]=nueva_coordenada
        
    def obtener_coordenada(self, borracho): 
        return self.coordnadas_borrachos[borracho]