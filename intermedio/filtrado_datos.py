# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 00:26:06 2021

@author: Asus
"""

DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]

def run():
    print("___________________________________________________________")
    all_python_names = [woker["name"] for woker in DATA if woker["language"] == "python"]
    langague_python = list(filter(lambda worker:  worker["language"]=="python" , DATA))
    #print(langague_python)
    all_python_names = list(map(lambda  worker: worker["name"], langague_python))
    print(all_python_names)
    print("_____________________________fin______________________________")
    all_platzi_workers = [{"name":worker["name"],"age":worker["age"]} for worker in DATA if worker["organization"]=="Platzi"]
    platzi_workers = list(filter(lambda workers:workers["organization"]=="Platzi", DATA))
    sall_platzi_workers = list(map(lambda  workers:workers["name"], platzi_workers))
    print(all_platzi_workers)
    print("_____________________________fin______________________________")
    adultos = [{"name": worker["name"], "edad":worker["age"]} for worker in DATA if worker["age"]>=18]
    print(adultos)
    #x = lambda y: y*5
    #print(x(2))
    adults = list(filter(lambda worker: worker["age"]>18, DATA))
    adults = list(map(lambda worker:worker["name"], adults))
    print(adults)
    print("________________________________________________________________")
       
    old_people = list(map(lambda worker: { "old": worker["age"]>18}  ,DATA))
    old_people = [{"name":workers["name"],"old":True} if workers["age"]>18
                  else{"name": workers["name"],"old":False} for workers in DATA ]
    #old_people = list(map(lambda worker: worker | {"old": worker["age"]>70}  ,DATA)) #3.9
    print(old_people)
    
if __name__ == "__main__":
    run()