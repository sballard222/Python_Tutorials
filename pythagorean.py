# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 11:38:37 2019

@author: sballard
"""

import math 

def pythagorean(a, b):
    hypotenuse_squared  = a**2 + b**2
    hypotenuse = math.sqrt(hypotenuse_squared)
    print("The hypotenuse is: ", hypotenuse)
    
    #call function 
    pythagorean(3,4)