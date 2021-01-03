# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 17:00:23 2018

@author: Robin
"""
lower_limit = int(input("Enter lower limit: "))
upper_limit = int(input("Enter upper limit: "))
    
for nums in range(lower_limit, upper_limit + 1):
    sum = 0
    for i in range(1, nums):
        if (nums % i) == 0:
            sum += i
    if nums == sum:
        print(nums, end=" ")

