# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 16:20:53 2024

@author: jacin
"""

class Solution(object):
    def reverseWords(self, s):
        #s.split converts the string into a list of separate words
        words = s.split()
        #Now we have a list so we can use the reverse methos
        words.reverse()
        #After reversing the list now convert it into its original form string using the join method
        reverse_string = ' '.join(words)
        return reverse_string

#join() is a method in Python that concatenates the elements of an iterable (like a list) single string.
# When reversing the words in a sentence, you want the words to be separated by a single space in the resulting string.
#Using a space as the separator ensures that there is exactly one space between each word in the final string, which matches the requirement.
#The string on which join() is called (' ' in this case) is used as the separator between the elements.

