# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 15:58:28 2020

@author: mnsah
void even_and_odd_numbers
(
	// Input array that contains even numbers and odd numbers
	int* inputArray,  
	// Element count of the input and output arrays
	int elementCount,  
	// Output array with even numbers at the beginning of 
	// the array followed by odd numbers
	int* outputArray   
)
{
    // Please write code here
}

Example:

elementCount = 8
inputArray  = { 4, 5, 3, 2, 6, 1, 8, 7 }

outputArray = { 4, 2, 6, 8, 5, 3, 1, 7 }

"""

def evenoddfinder(L):
#    odd = []
#    even = []
#    for l in L:
#        if l%2 == 0:
#            even.append(l)
#        else:
#            odd.append(l)
    for i in range(len(L)-1):
        if L[i]%2 != 0 :
            for j in range(i+1, len(L)):
                if L[j]%2 == 0:
                    temp = L[i]
                    L[i] = L[j]
                    L[j] = temp
                    break
     
    return L

inp = [4, 5, 3, 2, 6, 1, 8, 7]

print(evenoddfinder(inp))
            
        

