# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 10:29:48 2018

@author: Robin
"""

# Three-Year-Old Simulator
# Demonstrate the while loop

print("\tWelcome to the 'Three_Year_Old Simulator.\n")
print("This program simulates a conversation with a three-year-old child.")
print("Try to stop the madness.\n")

response = ""
while(response != "Because"):
    response = input("Why?\n")

    print("Oh! Okay.")