# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 02:27:25 2021

@author: abbos
"""

def qoldiqsiztekshir(son):
    for n in range(2,11):
        if son%n:
            print(son, n, "ga qoldiqsiz bo'linmaydi.")
        else:
            print(son, n, "ga qoldiqsiz bo'linadi.")
        n+=1
son=int(input("Sonni kiriting:\n>>>"))
qoldiqsiztekshir(son)










