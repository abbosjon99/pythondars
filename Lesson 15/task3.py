# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 02:08:13 2021

@author: abbos
"""

capital = {"usa" : 'Washington',
          "uk" : 'London',
    "germany" : 'Berlin',
    "czech republic" : 'Prague',
    "poland" : 'Warsaw',
    "russia" : 'Moscow'
    }
country  = input('Input any country name:\n>>>').lower()
capitall= capital.get(country)
if capitall==None:
    print("Sorry, we do'nt have this information. :(")
else:
    print(capitall.title())