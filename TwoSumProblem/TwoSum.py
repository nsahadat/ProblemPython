# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 14:52:33 2020

@author: mnsah

You are given a list of numbers, and a target number k. Return whether or not there are two numbers in the list that add up to k.
"""

def two_sum(L, k):
    for i in range(len(L)-1):
        for j in range(i,len(L)):
            if L[i] + L[j] == k:
                return True
            
    return False
        


print(two_sum([4,7,1,-3,2], 5))
# True

print(two_sum([4,0,-1,-3,2], 5))
# False

print(two_sum([], 5))
False