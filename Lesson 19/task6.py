# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 02:25:02 2021

@author: abbos
"""

def sonnidarajagakutar(x, y=2):
    print(f"{x} ning {y}-darajasi {x**float(y)} ga teng.")
x=float(input("X ni kiriting:\n>>>"))
y=input("Y ni kiriting:\n>>>")
if y:
    sonnidarajagakutar(x, y)
else:
     sonnidarajagakutar(x)