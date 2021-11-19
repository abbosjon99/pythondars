# -*- coding: utf-8 -*-
"""
Created on Sat Nov 20 02:09:00 2021

@author: abbos
"""

def mijozkirit(ismi, tyili, tjoyi, email=" ", traqam=None):
    malumotlar={
        "ismi":ismi,
        "tyili":tyili,
        "tjoyi":tjoyi,
        'email':email,
        'traqam':traqam
        }
    return malumotlar
mijozlar=[]
while True:
    print("Mijoz haqida kiriting:")
    ismi=input("Ismi:\n>>")
    tyili=int(input("Tug'ilgan yili:\n>>"))
    tjoyi=input("Tug'ilgan joyi:\n>>")
    email=input("Elekton pochtasi:(ixtiyoriy)\n>>")
    traqam=input("Telefon raqami:(ixtiyoriy)\n>>")
    mijozlar.append(mijozkirit(ismi, tyili, tjoyi, email, traqam))
    davomi=input("Davom ettirishni xoxlaysizmi? yes/no\n>>").lower()
    if davomi!='yes':
        break
for mijoz in mijozlar:
    print(f"{mijoz['ismi'].title()}, {mijoz['tyili']}-yil {mijoz['tjoyi'].title()} da tug'ilgan.\
\nElektron pochtasi: {mijoz['email']}, telefoni {mijoz['traqam']}")
