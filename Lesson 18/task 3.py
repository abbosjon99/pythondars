# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 23:25:43 2021

@author: abbos
"""

mahsulotlar={}
while True:
    mahsulot=input("Mahsulot nomini kiriting:\n(Tugatish uchun 'tugash' deb yozing)\n>>").lower()    
    if mahsulot=="tugash":
        break
    else:   
        narx=float(input(f"{mahsulot.title()} narxini kiriting:"))
        mahsulotlar[mahsulot]=narx
buyurtmalar=[]
while True:
    buyurtma=input("Buyurtma nomini kiriting:\n(Tugatish uchun 'tugash' deb yozing)\n>>").lower()    
    if buyurtma=="tugash":
        break
    else:   
        buyurtmalar.append(buyurtma)
while buyurtmalar:
    buyurtma=buyurtmalar.pop()
    if buyurtma in mahsulotlar:
        print(f"{buyurtma.title()} {mahsulotlar[buyurtma]} so'm")
    else:
        print(f"Bizda {buyurtma.title()} yo'q.")



