# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 16:06:26 2024

@author: jacin
"""

class Solution(object):
    def predictPartyVictory(self, senate):
       # convert the string to list 
        senate = list(senate)
       
       # Create 2 queues D and R
        D,R = deque(),deque()
       
       # 1) Create the 2 queues
       # for index , letter in the list senate 
       # Enumerate helps to get the index and the letter.
        for i,c in enumerate(senate):
           # Create the first queue
           if c == "R":
              # Append the index position to the R queue
              R.append(i)
           else:
              # Append the index position to the D queue
              D.append(i)   

        # 2) Perform the operation
        # While both the queues have elemets in it 
        while D and R: 
              # Initially pop the first elements of both the queues    
              dturn = D.popleft()
              rturn = R.popleft()
              
              # When the index popped at r queue is less than d queue , it means that r preceeds d
              # So r gets a chance to remove the rights of d 
              if rturn < dturn:
                # Add to  the R queue the rturn+len(senate)
                # see rturn got popped initially as part of the algorithm we did,but it removed the right 
                # of the next senator(dire) and its still there its not removed so add it+len(senate)
                # Why index + len(senate) Works
                # Future Turn: Adding index + len(senate) ensures that the defeated senator gets a future          #turn after a full cycle of the senate. 
                # This models the cyclic nature of the problem and allows the simulation to
                # progress towards a conclusion.
                 R.append(rturn + len(senate))

              else:
                 D.append(dturn + len(senate))  
        
        # at the end ,  if the R contains elements (if Radiant queue is not empty) return the value Radiant
        # If the dire queue is not empty then return the value as dire
        return "Radiant" if R else "Dire"         
