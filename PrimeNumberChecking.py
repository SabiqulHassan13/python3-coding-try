# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 23:23:51 2018

@author: Robin
"""

print("Checking for a number is whether prime or not")
num = int(input("Enter a positive integer: "))

if(num > 1):   
    isPrime = True
    
    for i in range(2, num):
        if(num % i == 0):
            isPrime = False
            break
    if(isPrime):
        print(num, " is a prime number")
    else:
        print(num, " is not a prime number")
        
else:
    print(num, " is not a prime number")