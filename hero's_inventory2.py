# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 19:23:50 2018

@author: Robin
"""

# Hero's Inventory 2.0
# Demonstrates tuple

# create a tuple with some items and display it with for loop
inventory = ("sword",
             "armor", "shield", "healing potion")
print("Your items: ")
for item in inventory:
    print(item)
    
input("\nPress the enter key to continue.")

# get the length of a tuple
print("You have", len(inventory), "items in your possesstion.")

input("\nPress the enter key to continue.")

# test for membership with in
if ("healing potion" in inventory):
    print("You will have to fight another day.")

# display one item through an index
index = int(input("Enter the index number for an item in inventory: "))
print("At index", index, "is", inventory[index])

# display a slice
start = int(input("\nEnter the index number to begin a slice: "))
finish = int(input("Enter the index number to end the slice: "))
print("inventory[", start, ":", finish, "] is", end = " ")
print(inventory[start : finish])
input("\nPress the enter key to continue.")

# concatenating tuples
chest = ("gold", "gems")
print("You find a chest. It contains:")
print(chest)

