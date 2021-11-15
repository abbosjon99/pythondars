# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 22:35:05 2021

@author: abbos
"""
print('Pytonda operatorlar izohli lug\'ati:')
dict={'integer':'butun sonlar to\'plami',
      'float':'haqiqiy sonnlar to\'plami',
      'if':'agar tarmoqlanuvchi operatori'
      }
oper=input('Operator nomini kiriting:\n>>>>>')
print(f"Ushbu {oper} operatori -", dict.get(oper.lower(), "ma'lumot yo'q"),"dir.") 
