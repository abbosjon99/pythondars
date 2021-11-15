# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 21:19:14 2021

@author: abbos
"""

kitoblar=[]
ishora=True;
while ishora:
    kitob=input("Yoqtirgan kitobingizni kiriting,tugatish uchun 'exit' deb yozing:\
\n>>>").lower()
    if kitob=="exit":
        ishora=False
    else:
        kitoblar.append(kitob)
print("Yoqtirgan kitoblaringiz:")
for kitob in kitoblar:
    print(kitob.title())
    
    