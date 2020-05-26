# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 16:15:45 2020

@author: mnsah
Given a list of numbers, where every number shows up twice except for one number, find that one number.

Challenge: Find a way to do this using O(1) memory.
"""

def singleNumber(nums):
    if nums == []:
        return None
    i = 0
    nums = sorted(nums)
    while i <len(nums)-1:
        if nums[i] != nums[i+1]:
            return nums[i]
        i += 2
        if i == len(nums)-1:
            return nums[i]
    return None
#        print(i)
    
  

print(singleNumber([4, 3, 2, 4, 1, 3, 2]))
# 1

print(singleNumber([4, 3, 2, 4, 1, 1, 3, 2, 10, 10, 11]))
# 11

print(singleNumber([10, 4, 3, 2, 4, 1, 1, 3, 2, 10, 11]))
# 11