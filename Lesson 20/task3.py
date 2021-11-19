# -*- coding: utf-8 -*-
"""
Created on Sat Nov 20 02:23:06 2021

@author: abbos
"""

def kattanitop(son1, son2, son3):
    """Uchta sonning eng kichigini aniqlaydi."""
    maxi=son1
    if son2>maxi:
        maxi=son2
    if son3>maxi:
        maxi=son3
    return maxi
son1 = float(input("Birinchi sonni kiriting: "))
son2 = float(input("Ikkinchi sonni kiriting: "))
son3 = float(input("Uchinchi sonni kiriting: "))
maxi=kattanitop(son1, son2, son3)

print('Eng kattasi:', maxi)
