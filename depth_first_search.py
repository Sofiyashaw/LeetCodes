# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 14:05:14 2024

@author: jacin
"""


def dfs(graph,start,visited=None):
    if visited is None:
        visited=set()
    visited.add(start)
    print(start,end=" ")
        
    for neighbour in graph.get(start,[]):
        if neighbour not in visited:
            dfs(graph,neighbour,visited)
                
                
graph = { 
    0:[1,2],
    1:[2],
    2:[0,3],
    3: [3] }
print("Depth First Traversal starting from vertex-2")     
dfs(graph,2)