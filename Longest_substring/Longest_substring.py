# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 12:11:21 2020

@author: mnsah

Given a string, find the length of the longest substring without repeating characters.
class Solution:
  def lengthOfLongestSubstring(self, s):
    # Fill this in.

print Solution().lengthOfLongestSubstring('abrkaabcdefghijjxxx')
# 10
"""

class Solution:
  def lengthOfLongestSubstring(s):
      smap = {}
      res = 0
      maxlen = 0
      for c in s:
          if c not in smap:
            smap[c] = 1
            res += 1
          else:
#            smap[c] += 1
            smap = {}
            res = 0
          if (res>maxlen):
              maxlen = res

      return maxlen
      
  

print(Solution.lengthOfLongestSubstring('abbbsssssttrrriijjkkllabcdefghijklopqrstuvwxyzzzzzzzzzzzzzttttttttttt'))
# 10