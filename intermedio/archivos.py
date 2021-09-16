# -*- coding: utf-8 -*-
"""
Created on Fri Aug 13 22:12:00 2021

@author: Asus
"""

def read():
    numbers = []
    with open("./archivos/archivo.txt", "r", encoding="utf-8") as f:
        for line in f:
            numbers.append(int(line))
    print(numbers)

def write(): 
    names = ["Arcadio", "Jesus", "Galí", "Juan", "Juana"]
    with open("./archivos/nombres.txt", "w", encoding="utf-8") as f:
        for name in names:
            f.write(name)
            f.write('\n')

        
def run():
    read()
    write()

if __name__ == '__main__':
    run()