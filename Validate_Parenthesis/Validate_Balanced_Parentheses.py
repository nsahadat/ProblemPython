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
    if s==[]:
            return True
    bmap = {}
    bmap[')'] = '('
    bmap['}'] = '{'
    bmap[']'] = '['
    stack = []
    
    # check every character O(N)
    for st in s:
        # if character in bmap
        if (st in bmap):
            # if stack nonempty then pop the element and compare with the hashmap
            if stack:
                top = stack.pop()
            else:
                top = '#'
            if top != bmap[st]:
                return False
        # if not push in to stack to pop later     
        else:
            stack.append(st)

    return stack == []
            


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
# should return False
print(Solution().isValid(s))

s = "([)]"
# should return False
print(Solution().isValid(s))