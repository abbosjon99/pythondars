# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 00:07:26 2021

@author: abbos
"""

son=int(input("Butun son kiriting: "))
for n in range(2,10):
    if not son%n:
        print (f"{son} {n} ga bo'linadi.")