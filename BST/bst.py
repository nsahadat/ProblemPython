# -*- coding: utf-8 -*-
"""
Created on Mon May 25 23:30:59 2020

@author: mnsah
"""

def bst(nums, target):
    left = 0
    right = len(nums)-1
    
    while left<=right:
        mid = left + (right-left)//2
        
        if target <= nums[mid]:
            right = mid - 1
        else:
            left = mid + 1
    
    return left

#bst that return left first target index

# testing code
nums = [0, 1, 2, 4, 5, 6, 6, 6, 7, 7, 7, 8, 9, 10]
print(bst(nums, 7))     # left target index
print(bst(nums, 7+1)-1) # right target index
            
    