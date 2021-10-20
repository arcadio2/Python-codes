# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 22:59:31 2021

@author: Asus
"""

import numpy as np
import  matplotlib.pyplot as plt
import random

def get_data():
    x = []
    y = []
    for i in range(100): 
        x.append((i+1)*random.randint(3,7))
        y.append((i+1)*random.randint(5,13))
        
    return x,y

def estimate(x,y):
    n = np.size(x)
    m_x, m_y = np.mean(x), np.mean(y)

    var = np.sum((x-m_x)**2)
    cov = np.sum((x-m_x)*(y-m_y))
    m = cov/var
    b = m_y - m*m_x

    return (m,b)


def ploting(x,y,b):     
    plt.scatter(x,y, color="g", marker="o", s=30)
    y_pred = b[0]*x + b[1]
    plt.plot(x,y_pred, color = "b")
    plt.xlabel("Independiente")
    plt.ylabel("Dependiente")
    
    plt.show()
    
def estimated(b,num): 
    return b[0]*num + b[1] 
    
    
if __name__ == '__main__':
    #x = np.array([1,2,3,4,5])    
    #y = np.array([2,3,5,6,5])
    x,y = get_data()
    x = np.array(x)
    y = np.array(y)
    b=estimate(x,y)

    print(f'Los valores de m ={b[0]} y b = {b[1]} ')
    ploting(x,y,b)
    print("____________________________________________")
    estimados = estimated(b,np.array([200,300,400]))
    
    
    
    