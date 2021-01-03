# -*- coding: utf-8 -*-
"""
Created on Sun Dec 30 11:57:07 2018

@author: Robin
"""

# Handle It
# Demonstrate handling exceptions

# try/ except
try:
    num = float(input("Enter a float number: "))
    
except ValueError:
    print("That was not a number.")
    print("Something went wrong!")
    
# handle multiple exception types
print()
for value in (None, "Hi!"):
    try:
        print("Attempting to convert", value, "-->", end = " ")
        print(float(value))
        
    except(TypeError, ValueError):
        print("Something went wrong!")
        
# multiple exception clauses
print()
for value in (None, "Hi!"):
    try:
        print("Attempting to convert", value, "-->", end = " ")
        print(float(value))
    except TypeError:
        print("I can only convert a string or a number!")
    except ValueError:
        print("I can only convert a string of digits!")
        
# get an exception's argument
try:
    num = float(input("\nEnter a number: "))
except ValueError as e:
    print("That was not a number! Or as Python would say...")
    print(e)
        
# adding an else clause
    # it will execute only if no exception is raised
try:
    num = float(input("\nEnter a number: "))
except ValueError as ex:
    print("That was not a number!", ex)
else:
    print("You entered the number", num)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        