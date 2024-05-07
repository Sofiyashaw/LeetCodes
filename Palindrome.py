#Write a Python Program to check whether a string is palindrome or not
"A palindrome is a word,Phrase,number or sequence of words that reads the same backward as forward e.g.Madam"


def ispalindrome(s):
    s = s.lower()
    s = ''.join(c for c in s if c.isalnum())
    return s == s[::-1]

string = input("Enter the string: ")
if ispalindrome(string):
    print("Palindrome")
else:
    print("Not a Palindrome")

    
    
    
    
    
    
    
   
    
    
   
    
    
    
    
    
    
    
    
    
   
