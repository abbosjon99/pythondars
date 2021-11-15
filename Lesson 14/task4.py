# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 22:48:50 2021

@author: abbos
"""

en_uz = {'apple':'olma',
    'pomegrenate':'anor',
    'grape':'uzum',
    'persimmon':'xurmo',
    'apricot':'o\rik'
    }
meva=input('Meva nomini kiriting:\n>>').lower()
meva=en_uz.get(meva)
if meva!=None:
    print(meva.title())
else: 
    print('So\'z mavjud emas.')