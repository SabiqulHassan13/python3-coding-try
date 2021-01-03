# -*- coding: utf-8 -*-
"""
Created on Sat Dec 15 10:44:00 2018

@author: Robin
"""

# Random Access
# Demonstrates string indexing

import random

word = "index"
print("The word is: ", word, "\n")

high = len(word)
low = -len(word)

# working with random position number
print("\nworking with random position number")
for i in range(10):
    position = random.randrange(low, high)
    print("word[", position, "]\t = ", word[position])
    
# working with positive position number
print("\nworking with positive position number")
for i in range(len(word)):
    print("Value of index: ", i, "is", word[i])


# working with negative position number
print("\nworking with negative position number")
print(word[-1]) # last index letter of word
print(word[-2])
print(word[-3])
print(word[-4])
print(word[-5])