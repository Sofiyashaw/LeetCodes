# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 16:05:51 2024

@author: jacin
"""

import collections
class RecentCounter(object):

    def __init__(self):
        self.q = collections.deque()
        

    def ping(self, t):
       self.q.append(t)
       while self.q[0] < t-3000:
           self.q.popleft()
       return len(self.q)   
# Step 1: Assume you call ping(1).
# self.q = [1]
# Deque size: 1
# No elements to remove (1 >= 1 - 3000).
# Return 1.

# Step 2: Call ping(100).
# self.q = [1, 100]
# Deque size: 2
# No elements to remove (1 >= 100 - 3000).
#Return 2.

#Step 3: Call ping(3001).
#self.q = [1, 100, 3001]
#Deque size: 3
#No elements to remove (1 >= 3001 - 3000).
#Return 3.
        


