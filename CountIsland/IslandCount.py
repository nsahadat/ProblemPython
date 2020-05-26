# -*- coding: utf-8 -*-
"""
Created on Mon May 25 23:53:42 2020

@author: mnsah
"""
# depth first search
def dfs(r,c):
    if r<0 or r>m-1 or c<0 or c>n-1 or graph[r][c]!= 1:
        return
    graph[r][c] = 0
    
    for i, j in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
        dfs(r+i, c+j)


# callinf the main function to find the number of islands
def countIsland(): 
    res = 0
    for i in range(m):
        for j in  range(n):
            if graph[i][j]==1:
                res+= 1
                dfs(i,j)
    
    return res

graph = [[1,1,0,0], [0,1,0,1], [1,0,1,1], [0,0,0,1]]
m = len(graph)
n = len(graph[0])
print(countIsland())    # print number of islands