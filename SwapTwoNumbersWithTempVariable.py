# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 19:56:02 2018

@author: Robin
"""

num1 = eval(input("Enter 1st number, num1: "))
num2 = eval(input("Enter 2nd number, num2: "))

print("Before swapping: ")
print("Value of num1 is", num1, " and Value of num2 is", num2)

# swpping two variables
temp = num1 
num1 = num2
num2 = temp

print("After swapping: ")
print("Value of num1 is", num1, " and Value of num2 is", num2)