# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 11:12:13 2018

@author: Robin
"""

# Loosing Battle
# Demonstrates the dreaded infinite loop

print("Your lone hero is surrounded by a massive army of trolls.")
print("Their decaying green bodies stretch out, melting into the horizon.")
print("Your hero unsheathes the sword for the last fight of his life.\n")

health = 10
trolls = 0
damage = 3

while(health > 0):
    trolls += 1
    health -= damage
    print("Your hero swings and defeats an evil troll. "\
          "but takes", damage, "damage points.\n")
    
print("Your hero fought valiantly and defeated", trolls, "trolls.")
print("But alas! your hero is no more.")

# press ctrl + C to stop the infinite loop
#input("\nPress the enter key to exit.")
    