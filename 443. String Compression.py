# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 10:14:35 2024

@author: jacin
"""

class Solution:
    def compress(self, chars: List[str]) -> int:
        write = 0  # This will track where to write the compressed result in the array
        i = 0      # This is used to loop through the array

        while i < len(chars):  # Loop through each character in the array
            char = chars[i]    # Get the current character
            count = 0          # This will count how many times the character repeats

            # Count how many times the current character repeats
            while i < len(chars) and chars[i] == char:
                i += 1
                count += 1

            # Write the character (always write the character once)
            chars[write] = char
            write += 1  # Move the write pointer to the next position

            # If the character repeats more than once, write the count as well
            if count > 1:
                # Convert the count to a string and write each digit of the count
                for digit in str(count):
                    chars[write] = digit
                    write += 1

        return write  # Return the length of the compressed array
