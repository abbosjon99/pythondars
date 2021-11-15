# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 21:59:40 2021

@author: abbos
"""

buyurtmalar=[]
while True:
    buyurtma=input("Mahsulot nomini kiriting:\n(Chiqish uchun 'exit' deb yozing)\n>>")    
    if buyurtma.lower()=="exit":
        break
    else:   
        buyurtmalar.append(buyurtma)
print("Mahsulotlar ro'yhati:")
for mahsulot in buyurtmalar:
    print(mahsulot.title(), end=', ')




