# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 20:04:06 2018

@author: Robin
"""

num1 = eval(input("Enter num1: "))
num2 = eval(input("Enter num2: "))

print("-----------------------------------------------------")
print("Before Swapping,")
print("value of num1 is", num1, " and value of num2 is", num2)
print("-----------------------------------------------------")

num1 = num1 + num2
num2 = num1 - num2
num1 = num1 - num2

print()
print("-----------------------------------------------------")
print("After Swapping,")
print("value of num1 is", num1, "and value of num2 is", num2)
print("-----------------------------------------------------")

