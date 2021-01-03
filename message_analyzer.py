# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 12:37:59 2018

@author: Robin
"""

# Message Analyzer
# Demonstrate the len() function and the in operator

message = input("Enter a message: ")
print("\nThe length of your message", message, "is", len(message))

# counting vowel no in message
count_vowel = 0
count_consonant = 0 
count_white_space = 0
count_digit = 0

for letter in message:
    if (letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u'):
        count_vowel += 1
    elif (letter == 'A' or letter == 'E' or letter == 'I' or letter == 'O' or letter == 'U'):
        count_vowel += 1
    elif(letter == ' '):
        count_white_space += 1
    elif(letter >= '1' or letter <= '9'):
        count_digit += 1
    else:
        count_consonant += 1
    
print("No of vowel in", message, "is", count_vowel)        
print("No of consonant in", message, "is", count_consonant)        
print("No of white space in", message, "is", count_white_space)        
print("No of digit in", message, "is", count_digit) 

print("\nThe most common letter in the English language. 'e'.")
if "e" in message:
    print("is in your message.")
else:
    print("is not in your message.")