# -*- coding: utf-8 -*-
"""
Created on Sat Dec 15 11:13:37 2018

@author: Robin
"""
# No Vowels
# Demonstrates creating new string with a for loop

message = input("Enter a message: ")
new_message = ""
VOWELS = "aeiou"

print()
for letter in message:
    if(letter.lower() not in VOWELS):
        new_message += letter
        print("A new string has been created: ", new_message)
