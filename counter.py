# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 12:29:07 2018

@author: Robin
"""

# Counter
# Demonstrate the range() function

print("Counting:")
for i in range(10):
    print(i, end = " ")
    
print("\nCounting by fives:")
for i in range(0, 50, 5):
    print(i, end = " ")
    
print("\nCounting backwards:")
for i in range(10, 0, -1):
    print(i, end = " ")