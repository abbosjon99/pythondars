# -*- coding: utf-8 -*-
"""
Created on Sat Nov 20 02:52:27 2021

@author: abbos
"""

def tubson(son1,son2):
    "Berilgan oraliqdagi tub sonlarni chiqaruchi dastur"
    tublar=[]
    while son1<=son2:
        n=2
        while n<=son1:
            if n==son1:
                tublar.append(son1)
                break
            if son1%n==0:
                break
            n+=1
        son1+=1
    return tublar
son1=int(input("Oraliq boshini kiring: "))
son2=int(input("Oraliq oxirini kiring: "))
if son1*son2>0 and son1!=son2:
    tublar=tubson(son1,son2)
    print(tublar) 
else:
    print("Noto'g'ri oraliq kiritdingiz!!!!")









