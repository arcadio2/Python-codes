# -*- coding: utf-8 -*-
"""
Created on Sun Oct  3 00:59:38 2021

@author: Asus
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.array([0,1,2,3,4,5,6,7,8])
y = np.array([1,2,3,5,4,6,8,7,9])

coeff = np.polyfit(x,y,1)

print(coeff)


a = coeff[0]
b = coeff[1] 

# y=mx+b
est_y = (a*x) +b

print("Y = ",est_y)

plt.plot(x, est_y)
plt.scatter(x,y)
plt.show()