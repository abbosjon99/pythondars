# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 03:09:53 2021

@author: abbos
"""

lovely_films = { "Ibrohim" : ['Terminator', 'Avatar', 'Venom'],
    "Shakhzod" : ['Pulp Fiction', 'Insception', 'The Avengers'],
    "Sasha" : ['Hulk', 'Transformers', 'Joker'],
    "Clara" : ['Tom and Jerry', 'Masha and Bear', 'The Pink Panther'],
    }
for name, movies in lovely_films.items():
    print(name, "likes movies like:")
    for movie in movies:
        print(movie, end=', ')
    print()