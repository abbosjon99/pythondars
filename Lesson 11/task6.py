# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 23:44:34 2021

@author: abbos
"""

foydalanuvchilar=['admin', 'user', 'acer', 'lenovo', 'dell']
for n in range(5):
    login=input("Yangi loginni kiriting: ")
    if login.lower() in foydalanuvchilar:
        print("Login band, yangi login tanlang!")
    else:
        print("Xush kelibsiz, foydalanuvchi!")
        