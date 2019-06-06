# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 14:09:14 2019

@author: mnsah
"""

def fib(i):
    if i==1 or i == 2:
        result = 1
    else:
        result = fib(i-1) + fib(i-2)
        
        
    return result


print (fib(13))