# -*- coding: utf-8 -*-
"""
Created on Sat Nov 20 02:34:58 2021

@author: abbos
"""

def aylana(radius):
    aylana={
        'radius' : radius,
        'diametr' : radius*2,
        'perimetr' : radius*2*3.1415,
        'yuzi' : 3.1415*radius**2        
        }
    return aylana
radius = float(input("Aylana radiusini kiriting: "))
print(aylana(radius))


    
    
    
    
    
    
    