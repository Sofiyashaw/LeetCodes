# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 15:34:58 2024

@author: jacin
"""

# Python program to implement breadth first search

from collections import deque

def bfs(graph,start):
    visited = set()
    queue = deque([start])

    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            print(vertex, end=" ")
            visited.add(vertex)
            queue.extend(graph[vertex])
            
graph = { 0:[1,2],
          1:[2],
          2:[0,3],
          3:[3]
          } 
print("Breadth first traversal starting from vertex 2:") 
bfs(graph,2)          