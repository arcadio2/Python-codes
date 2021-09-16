# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 16:34:15 2021

@author: Asus
"""

class Persona: 
    def __init__(self, nombre):
        self.nombre=nombre 
        
    def avanza(self): 
        print("Ando caminando")
        

class Ciclista(Persona):  #Aqui son las hijas, dentro
    
    def __init__(self, nombre):
        super().__init__(nombre)
        
    def avanza(self): 
        print("ME muevo en bici") # ya es el polimorfismo, se convierte. 
        
def main(): 
    persona=Persona('David')
    persona.avanza()
    
    ciclista = Ciclista('Gali')
    ciclista.avanza()

if __name__ == '__main__':
    main()
    for i in range(2):
        print(i)
    