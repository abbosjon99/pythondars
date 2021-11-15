# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 02:32:45 2021

@author: abbos
"""

famous1 = {"name" : "Elon Musk",
    "born" : "1971",
    "hair" : "yellow",
    "sex" : "man"
    }
famous2 = {"name" : "Jeff Bezos",
    "born" : "1964",
    "hair" : "bald",
    "sex" : "man"
    }
famous3 = {"name" : "Bill Gates",
    "born" : "1955",
    "hair" : "black",
    "sex" : "man"
    }
famous0 = {"name" : "Ariana Grande",
    "born" : "1993",
    "hair" : "blonde",
    "sex" : "woman"
    }
sex1="His"
famouses=[famous1, famous2, famous3, famous0]
for famous in famouses:
    if (famous['sex']!='man'): sex1="Her"
    print(f"{famous['name'].title()} was born in {famous['born']}.\
 {sex1} hair is {famous['hair']}.")
