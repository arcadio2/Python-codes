# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 00:25:20 2021

@author: Asus
"""

def bayes(prior_A, prob_B_dado_A, prob_B):
    return (prior_A* prob_B_dado_A)/prob_B

if __name__ == '__main__':
    prob_cancer = 1/100000 # poblacion que tiene cancer
    prob_sintoma_dado_cancer = 1 # sintomas dado que tienen cancer, positivo a cancer
    #TODOS LOS PACIENTES CON CANCWE TIENEN SINTOMAS, según esto
    prob_sintoma_dado_no_cancer = 10/99999 # sintomas, pero no cancer}
    #La probabilidad de tener sintomas dado que salio negativo es 10/99999
    prob_no_cancer = 1- prob_cancer
    
    prob_sintoma = (prob_sintoma_dado_cancer*prob_cancer) + (prob_sintoma_dado_no_cancer*prob_no_cancer)
    
    prob_cancer_dado_sintomas = bayes(prob_cancer,prob_sintoma_dado_cancer, prob_sintoma)
    print(prob_cancer_dado_sintomas)