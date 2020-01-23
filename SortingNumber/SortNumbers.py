# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 15:08:33 2020

@author: mnsah

Given a list of numbers with only 3 unique numbers (1, 2, 3), sort the list in O(n) time.
"""
import collections

def sortNums(nums):
    smap = collections.Counter(nums)
    L = []
    for sm in sorted(smap):
        L += smap[sm]*[sm]
        
    return L

def sortNumsConstantSpace(nums):
    for i in range(len(nums)-1):
        for j in range(i,len(nums)):
            if nums[i]>nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
    return nums
  

print(sortNumsConstantSpace([3, 3, 2, 1, 3, 2, 1]))
# [1, 1, 2, 2, 3, 3, 3]

print(sortNums([3, 3, 2, 1, 3, 2, 1]))
# [1, 1, 2, 2, 3, 3, 3]