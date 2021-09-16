# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 21:42:56 2021

@author: Asus
"""

class Lavadora:
    
    def __init__(self):
        self._idk=None
        pass 
    
    def lavar(self,temperatura='caliente'):
        self._llenar_tanque_de_agua(temperatura)
        self._añadir_jabon()
        self._lavar()
        self._centrifugar()
    
    def _llenar_tanque_de_agua(self, temperatura):
        print(f'Llenando el tanque con agua {temperatura}')
        
    def _añadir_jabon(self):
        print("Añadiendo jabón")
    
    def _lavar(self): 
        print("Lavando ropa por fin")
        
    def _centrifugar(self):
        print("Centrifugando la ropa")
    #_ es que es metodo privado 
    @property #Getter
    def idk(self):
        return self._idk 
    #Setter
    @idk.setter
    def idk(self, idk):
        self._idk=idk
    
    
    
if __name__ == '__main__':
    lavadora = Lavadora()
    lavadora.lavar(temperatura="fría")