# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 21:39:26 2024

@author: jacin
"""

class Solution:
    def addMinimum(self, word: str) -> int:
        count = 0  # To keep track of insertions
        i = 0  # Pointer to iterate over the string

        while i < len(word):
            # First we check if the current character should be 'a'
            if word[i] == 'a':  
                i += 1  # Move to next character
            else:
                count += 1  # If not 'a', we need to insert 'a'

            # Now we check if the next character should be 'b'
            if i < len(word) and word[i] == 'b':  
                i += 1  # Move to next character
            else:
                count += 1  # If not 'b', we need to insert 'b'

            # Finally, check if the next character should be 'c'
            if i < len(word) and word[i] == 'c':  
                i += 1  # Move to next character
            else:
                count += 1  # If not 'c', we need to insert 'c'

        return count
