# -*- coding: utf-8 -*-
"""
Created on Sat Nov 20 01:44:27 2021

@author: abbos
"""
def malumotkirit(ismi, tyili, tjoyi, email=" ", traqam=None):
    malumotlar={
        "ismi":ismi,
        "tyili":tyili,
        "tjoyi":tjoyi,
        'email':email,
        'traqam':traqam
        }
    return malumotlar
ismi=input("Ismingizni kiriting:\n>>")
tyili=int(input("Tug'ilgan yilingizni kiriting:\n>>"))
tjoyi=input("Tug'ilgan joyingizni kiriting:\n>>")
email=input("Elekton pochtangizni kiriting:(ixtiyoriy)\n>>")
traqam=input("Telefon raqamingizni kiriting:(ixtiyoriy)\n>>")
malumotlar=malumotkirit(ismi, tyili, tjoyi, email, traqam)



