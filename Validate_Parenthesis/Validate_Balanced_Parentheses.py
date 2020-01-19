# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 10:08:55 2020

@author: mnsah
Imagine you are building a compiler. Before running any code, the compiler must check that the parentheses in the program are balanced. Every opening bracket must have a corresponding closing bracket. We can approximate this using strings.

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
- Open brackets are closed by the same type of brackets.
- Open brackets are closed in the correct order.
- Note that an empty string is also considered valid.
"""

class Solution:
  def isValid(self, s):
    # Fill this in.
    if len(s)==0:
        return True
    brmap = {}
    brmap['('] = 0
    brmap['{'] = 0
    brmap['['] = 0
    
    for st in s:
        if (st == '(' or st =='{' or st=='['):
           brmap[st] += 1
        else:
            if(st == ')'):
                brmap['('] -= 1
            elif (st == '}'):
                brmap['{'] -= 1
            elif (st == ']'):
                brmap['['] -= 1
            
            if any([brmap[b] == -1 for b in brmap]):
                return False
#        print (brmap)
    
    if any([brmap[b] != 0 for b in brmap]):
#        print('here')
        return False
    else:     
        return True
            


# Test Program
s = "()(){(())" 
# should return False
print(Solution().isValid(s))

s = ""
# should return True
print(Solution().isValid(s))

s = "([{}])()"
# should return True
print(Solution().isValid(s))

s = ")[{}])()"
# should return False
print(Solution().isValid(s))

s = "([{}])(){"
# should return False
print(Solution().isValid(s))

s = "({}])()"
# should return False
print(Solution().isValid(s))

s = "((((({{{{{)))))[[[[[}}}}}]]]]]"
# should return True
print(Solution().isValid(s))