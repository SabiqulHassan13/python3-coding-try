# -*- coding: utf-8 -*-
"""
Created on Tue Jan  1 11:01:46 2019

@author: Robin
"""

# Birthday wishes
# Demonstrates keyword arguments and default parameter values

# positional parameters
def birthday1(name, age):
    print("Happy Birthday,", name, "!", "I hear you're", age, "today.\n")
    
# parameters with default values
def birthday2(name = "Jackson", age = 1):
    print("Happy Birthday,", name, "!", "I hear you're", age, "today.\n")
    
# main
print("implementation of birthday1() function")
birthday1("Jackson", 1)
birthday1(1, "Jackson")
birthday1(name = "Jackson", age = 1)
birthday1(age = 1, name = "Jackson")

print("implementation of birthday2() function")
birthday2()
birthday2(name = "Katherine")
birthday2(age = 12)
birthday2(name = "Katherine", age = 12)
birthday2("Katherine", 12)
birthday2(12, "Katherine")

input("\nPress the enter key to exit.")