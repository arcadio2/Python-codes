# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 13:42:07 2021

@author: Asus
"""

from bokeh.plotting import figure, output_file, show

if __name__ == '__main__':
    output_file('Graficado_simple.html')
    fig = figure()
    tol_vals = int(input("Cuantos valores quieres graficar? "))
    x_vals = list(range(tol_vals))
    y_vals = []
    
    for x in x_vals:
        val = int(input(f'Valor de  y para {x}: '))
        y_vals.append(val)
    fig.line(x_vals, y_vals,line_width=2)
    show(fig)