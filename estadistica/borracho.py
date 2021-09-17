# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 22:56:08 2021

@author: Arcadio
"""
import random

class Borracho:
    
    def __init__(self, nombre): 
        self.nombre=nombre
        
class BorrachoTradicional(Borracho): 
    
    def __init__(self, nombre): 
        super().__init__(nombre)
        
    def camina(self): 
        return random.choice([(0,1),(0,-1), (1,0), (-1,0)])
    
        