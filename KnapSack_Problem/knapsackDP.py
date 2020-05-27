# -*- coding: utf-8 -*-
"""
Created on Tue May 26 23:50:43 2020

@author: mnsah
"""

def knapsack(values, weight, c):
    # vlues or profit that we have to maximize
    # weight for the each item
    # C capacity of the sack
    
    dp = [[0]*(c+1) for _ in range(len(values)+1)]
    
    for i in range(1,len(values)+1):
        for w in range(1,c+1):
            if weight[i-1]>w:
                dp[i][w] = dp[i-1][w]
            else:
                dp[i][w] = max(values[i-1]+dp[i-1][w-weight[i-1]], dp[i-1][w])
    print(dp)
    return dp[len(values)][c]

values = [150, 200, 300]
weight = [1, 3, 4]
capacity = 4

print(knapsack(values, weight, capacity))
            