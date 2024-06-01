# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 18:01:01 2024

@author: jacin
"""

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        ransomNoteCount = {}
        magazineCount = {}

        # Count frequencies in ransomNote
        for char in ransomNote:
            if char in ransomNoteCount:
                ransomNoteCount[char] += 1
            else:
                ransomNoteCount[char] = 1

        # Count frequencies in magazine
        for char in magazine:
            if char in magazineCount:
                magazineCount[char] += 1
            else:
                magazineCount[char] = 1

        # Check if each character in ransomNote has enough occurrences in magazine
        for char, count in ransomNoteCount.items():
            if magazineCount.get(char, 0) < count:
                return False

        return True

# Example usage
ransomNote = "a"
magazine = "b"
sol = Solution()
print(sol.canConstruct(ransomNote, magazine))  # Output: False
