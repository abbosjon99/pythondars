# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 02:14:07 2021

@author: abbos
"""
def kattakichiktop(son1, son2):
    if son1==son2:
        print("Sonlar teng.")
    elif son1>son2:
        print(son1, son2, "dan katta.")
    else:
        print(son2, son1, "dan katta.")
son1=float(input("Birinchi sonni kiriting:\n>>"))
son2=float(input("Ikkinchi sonni kiriting:\n>>"))
kattakichiktop(son1,son2)











