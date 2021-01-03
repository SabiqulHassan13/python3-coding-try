# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 18:55:49 2018

@author: Robin
"""

lower = int(input("Enter lower interval: "))
upper = int(input("Enter upper interval: "))


for num in range(lower, upper + 1):
    if(num > 1):
        for i in range(2, num):
            if(num % i == 0):
                #isPrime = False
                break
        else:
            print(num)
        
