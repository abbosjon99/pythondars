# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 03:01:26 2021

@author: abbos
"""

famous1 = {"name" : "Elon Musk",
    "born" : "1971",
    "hair" : "yellow",
    "sex" : "man",
    'novel': ['Elon Musk: Tesla, SpaceX, and the Quest for a Fantastic Future' ,'Superintelligence: Paths, Dangers, Strategies' ]
    }
famous2 = {"name" : "Jeff Bezos",
    "born" : "1964",
    "hair" : "bald",
    "sex" : "man",
    'novel': ['The Everything Store' ,'The Remains of the Day', 'Built to Last : Successful Habits of Visionary Companies']   }
famous3 = {"name" : "Bill Gates",
    "born" : "1955",
    "hair" : "black",
    "sex" : "man",
    'novel': ['How to Avoid a Climate Disaster' ,'The Road Ahead' ]
    }
famous0 = {"name" : "Ariana Grande",
    "born" : "1993",
    "hair" : "blonde",
    "sex" : "woman",
    'novel': ['Ariana Grande for Easy Piano Songbook' ,'Ariana Grande - Thank U, Next Songbook' ]
    }
sex="His"
famouses=[famous1, famous2, famous3, famous0]
for famous in famouses:
    if (famous['sex']!='man'): sex="Her"
    print(f"{famous['name'].title()} was born in {famous['born']}.\
 {sex} hair is {famous['hair']}.")
    print(sex, 'famous books:')   
    for novel in famous['novel']:
        print(novel)
