# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 18:57:07 2026

@author: 87727
"""


import random

# get random numbers
a = random.randint(1,10)
b = random.randint(1,10)
c = random.randint(1,10)

#show a,b,c
print(a)
print(b)
print(c)


#logic determine
if a > b :
    if b > c :        
        print(a,b,c)
        
    elif a > c:
        print(a,c,b)
        
    else:
        print(c,a,b)
        
elif b > c:    
    print(" ")    
    
else:
    print(c,b,a)
        

