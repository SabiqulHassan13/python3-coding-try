# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 09:30:21 2018

@author: Robin
"""

# Guess my Number generator games
import random

print("\tWelcome to 'Guess My Number'!")
print("\nI'm thinking of a number between 1 and 100.")
print("Try to guess it as few attempts as possible.")

random_num = random.randint(1, 100)
num = ""

while (random_num != num):
    num_count_time = 0
    num = int(input("Take a guess: "))

    if(num == random_num):
        num_count_time += 1
        print("You guessed it! The number was", num)
        print("And it only took you", num_count_time, "tries!")
    elif(num > random_num):
        num_count_time += 1
        print("Upper...")
        print("Random number was", random_num, "and you pressed", num)
    elif(num < random_num):
        num_count_time += 1
        print("Lower...")
        print("Random number was", random_num, "and you pressed", num)
        
        