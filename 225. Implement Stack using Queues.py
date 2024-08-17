# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 16:07:54 2024

@author: jacin
"""

class MyStack(object):
    # In stack we add at the end and remove at the end
    # In queue we add at the end and remove from the start
    # All the other operations are similar in stack and queue except for pop
    # So in popping  we pop the queue , and then add it to the end and we keep to do that until the 
    # last element is left and we return it 

   
    def __init__(self):
        # In this prob, we are doing only one queue
        # Initialize a dequeue
        self.q = deque()
        

    def push(self, x):
        # This is for adding operation
        self.q.append(x)

    def pop(self):
        # For popping pop the element  and add it back to the queue and return the last popped value
        for i in range(len(self.q) - 1):
            self.push(self.q.popleft())
        return self.q.popleft()
          
        # self.q[-1] returns the value of the top element  
    def top(self):
         return self.q[-1]


       # if the queue is empty return True , else return False
    def empty(self):
         return len(self.q) == 0

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()