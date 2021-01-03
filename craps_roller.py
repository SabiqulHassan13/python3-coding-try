# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 09:18:32 2018

@author: Robin
"""

# Craps Roller
# Demonstrate random numbers generation
# importing random module
import random

# generate random numbers between 1 - 6
die1 = random.randint(1, 6)
die2 = random.randrange(6) + 1

total = die1 + die2
print("You rolled a", die1, "and a", die2, "for a total of", total)