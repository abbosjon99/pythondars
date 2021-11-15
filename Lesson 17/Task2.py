# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 21:42:54 2021

@author: abbos
"""

while True:
    yosh=input("Yoshni kitiring(tugatish uchun 'exit' kiriting): \n>>")
    if yosh=="exit":
        break
    yosh=int(yosh)
    if yosh<7 or yosh>=65:
        print("Bepul")
    elif yosh<19:
        print("3000 so'm")
    else:
        print("10000 so'm")
    
    