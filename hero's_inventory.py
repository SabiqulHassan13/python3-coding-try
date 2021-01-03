# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 18:40:24 2018

@author: Robin
"""

# hero's inventory
# demonstrates tuple creation

# create an empty tuple as condition
inventory = ()

# treat the tuple as a conditioin
if (not inventory):
    print("You are empty-handed.")
    
input("\nPress the enter key to continue.")

# create a tuple with some items
inventory = ("sword",
             "armor",
             "shield",
             "healing potion")

# print the tuple 
print("\nThe tuple inventory is: ")
print(inventory)

# print each element in the tuple
print("\nYour items: ")
for item in inventory:
    print(item)
    
print("\nPress the enter key to exit.")