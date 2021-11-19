# -*- coding: utf-8 -*-
"""
Created on Sat Nov 20 03:36:05 2021

@author: abbos
"""

def fibonachchitop(son):
    fibonachchi=[]
    for n in range(son+1):
        if n==0 or n==1:
            fibonachchi.append(n)
        elif n==2:
            fibonachchi.append(1)
            fibonachchi.append(n)
        else:
            if n==fibonachchi[-1]+fibonachchi[-2]:
                fibonachchi.append(n)
    return fibonachchi
son=int(input("Oraliq oxirini kiring: "))
if not son<0:
    fibonachchi=fibonachchitop(son)
    print(fibonachchi) 
else:
    print("Noto'g'ri oraliq kiritdingiz!!!!")
            
    











