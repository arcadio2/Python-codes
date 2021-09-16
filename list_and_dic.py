# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""
import math
from functools import reduce
def run():
    my_list=[1,"Hello",True,4.5]
    my_dict = {"firstname":"Arcadio", "lastname":"López"}
    
    super_list = [
            {"firstname":"Arcadio", "lastname":"López"},
            {"firstname":"Jesus", "lastname":"López"},
            {"firstname":"Juan", "lastname":"López"},
            {"firstname":"Gali", "lastname":"López"}
        ]
    
    super_dict = {
        "natural_nums":[1,2,3,4,5],
        "integer_nums": [-1,-2,0,1,2],
        "floating_nums": [1.2,4.1,2.2]
        }
    
    
    for key, value in super_dict.items():
        print("Key","-",value)
    
    
    for dic in super_list:
        print("Diccionario ", dic)
    
    
    numeros_nat = []
    for i in range(1,101):
        if (i%3!=0):
            cuadrado = i**2
            numeros_nat.append(cuadrado)
    print(numeros_nat)
    
    squares = [i**2 for i in range(1,101) if i%3!=0]
    print(squares)
    
    list_compreshion = [i for i in range(1,9999) if (i%4==0 and i%6==0 and i%9==0)]
    print("--------------------------------------------")
    print(list_compreshion)
    
    
    dict_1 = {i:i**3 for i in range(1,101) if i%3!=0}
    print("--------------------------------------------")
    print(dict_1)
    print("--------------------------------------------")
    
    dic_sqrt = {i:math.sqrt(i) for i in range(1,1001) }
    print(dic_sqrt)
    
    mifuncion = lambda a,b: a*b
    
    print(mifuncion(2,5))
    
    print("--------------------------------------------")
    my_list = [1,4,5,6,9,13,19,21]
    odd = list(filter(lambda x: x%2!=0, my_list))
    print(odd)
    print("--------------------------------------------")
    list_1 = [1,2,3,4,5]
    
    list_2 = [i**2 for i in list_1 ]
    print(list_2)
    
    squares = list(map(lambda x:x**2, list_1))
    print(squares)
    "REDUCE"
    print("--------------------------------------------")
    list_reduce =[2,2,2,2,2]    
    all_multipled = reduce(lambda a,b:a*b, list_reduce)
    print(all_multipled)
    
if __name__ == "__main__":
    run()