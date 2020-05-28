# -*- coding: utf-8 -*-
"""
Created on Thu May 28 08:50:58 2020

@author: mnsah
"""

def findLPS(pattern):
    m = len(pattern)
    lps = [0]*m
    ln = 0
    i = 1
    
    while i<m:
        if pattern[i]==pattern[ln]:
            ln += 1
            lps[i] = ln
            i+=1
        else:
            if ln>0:
                ln = lps[ln-1]
            else:
                i += 1
    return lps

def findMatch(txt, pat):
    n = len(txt)
    m = len(pat)
    i = 0
    j = 0
    
    lps = findLPS(pat)
    while i<n:
        if txt[i]==pat[j]:
            i+=1
            j+=1
            if j==m:
                print('pattern found ' + str(i-j))
                j = lps[j-1]
        else:
            if j>0:
                j = lps[j-1]
            else:
                i += 1

txt = "ABABDABACDABABCABABABABCABAB"
pat = "ABABCABAB"
findMatch(txt, pat)
                
                
                
