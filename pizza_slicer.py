# -*- coding: utf-8 -*-
"""
Created on Sat Dec 15 11:33:22 2018

@author: Robin
"""

# Pizza Slicer
# Demonstrates string slicing

word = "pizza"

print("""
          Slicing 'Cheat Sheet'
      
      0    1    2    3    4    5
      +----+----+----+----+----+
      | p  | i  | z  | z  | a  |
      +----+----+----+----+----+
      -5  -4   -3   -2   -1
      """)

print("Enter the beginnning and ending index for your slice of 'pizza'.")
print("Press the enter key at 'Start' to exit.")
start = None
while(start != ""):
    start = (input("\nStart: "))
    
    if(start):
        start = int(start)
        finish = int(input("Finish: "))
        
        print("word[", start, ":", finish, "] is", end = " ")
        print(word[start : finish])
    
print("\n\nPress the enter key to exit.")