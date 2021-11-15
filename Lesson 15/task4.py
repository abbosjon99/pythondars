# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 02:17:22 2021

@author: abbos
"""

menu = {
        'osh':20000,
        "lag'mon":22000,
        'non':4000,
        'choy':5000,
        'shashlik':12000,
        'somsa':6000,
        'tabaka':15000
        }
dishes=[]
for n in range(3) :
    dishes.append(input(f"{n+1}-ovqat nomini kiriting:\n>>").lower())
for dish in dishes:
    if dish in menu:
        print(dish.title(), f"narxi {menu[dish]} so'm.")
    else:
        print("Bizda", dish, "yo'q.")
    















