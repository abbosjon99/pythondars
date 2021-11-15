# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 03:18:21 2021

@author: abbos
"""

Davlatlar = { 
    "usa" : {
    "capital":'Washington',
    "independence" : '1776',
    "language" : "Enlish",
    "cities" :  ['New York', 'Texas', 'San Francisco']   
    },
    "uzbekistan" : {
    "capital":'Tashkent',
    "independence" : '1991',
    "language" : "Uzbek",
    "cities" :  ['Qarshi', 'Samarkand', 'Nukus']   
    },
    "russia" : {
    "capital":'Moscow',
    "independence" : '1991',
    "language" : "Russian",
    "cities" :  ['Saint Peterburg', 'Edinburg', 'Sochi']   
    },
    "germany" : {
    "capital":'Berlin',
    "independence" : '1990',
    "language" : "German",
    "cities" :  ['Munich', 'Hamburg', 'Frankfurt']   
    }
    }
for davlat, informations in Davlatlar.items():
    print(f"{davlat.title()}ning poytaxti {informations['capital']}.\n\
Mustaqillikka {informations['independence']}-yili erishgan.\n\
Davlat tili {informations['language']}. Katta shaharlari:")
    for city in informations['cities']:
        print(city)