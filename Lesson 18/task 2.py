# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 23:17:28 2021

@author: abbos
"""

mahsulotlar={}
while True:
    mahsulot=input("Mahsulot nomini kiriting:\n(Chiqish uchun 'exit' deb yozing)\n>>")    
    if mahsulot.lower()=="exit":
        break
    else:   
        narx=float(input(f"{mahsulot.title()} narxini kiriting:"))
        mahsulotlar[mahsulot]=narx
print("Mahsulotlar ro'yhati:")
for k, v in mahsulotlar.items():
    print(k.title(), "=", v)