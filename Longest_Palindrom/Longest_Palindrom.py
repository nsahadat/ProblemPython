# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 11:55:08 2020

@author: mnsah

A palindrome is a sequence of characters that reads the same backwards and forwards. Given a string, s, find the longest palindromic substring in s.

Example:
Input: "banana"
Output: "anana"

Input: "million"
Output: "illi"
class Solution: 
    def longestPalindrome(self, s):
      # Fill this in.
        
# Test program
s = "tracecars"
print(str(Solution().longestPalindrome(s)))
# racecar
"""

class Solution: 
    def longestPalindrome(self, s):
      # Fill this in.
      #res = []
      def reverse(st):
          return st[::-1]
      mlen = 1
      for i in range(2,len(s)):
          for j in range(len(s)-i):
              if s[j:j+i+1] == reverse(s[j:j+i+1]) and i>mlen:
                  res = s[j:j+i+1]
                  mlen = len(res)
      #print(res)
      
      return res
          
        
# Test program
s = "idonotonodi"
print(str(Solution().longestPalindrome(s)))
# racecar