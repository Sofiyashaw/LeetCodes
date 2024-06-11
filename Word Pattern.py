# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 19:01:16 2024

@author: jacin
"""

class Solution(object):
    def wordPattern(self, pattern, s):
        words = s.split()

        if len(pattern) != len(words):
            return False

        char_to_word = {}
        word_to_char = {}

        for char,word in zip(pattern,words):
            if char in char_to_word:
                if char_to_word[char] != word:
                    return False
            else:
                    char_to_word[char] = word  

            if word in word_to_char:
                if word_to_char[word] != char:
                    return False
            else:
                    word_to_char[word] = char

        return True
pattern = "abba"
s = "dog cat cat dog"
sol = Solution()
sol.wordPattern(pattern,s)                      
                    

           