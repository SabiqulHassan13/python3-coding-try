# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 10:59:46 2018

@author: Robin
"""
# sentry variable update
# counter is a sentry variable here
# if you don't update the value of sentry variable then the loop will be infinite
# use ctrl + C to terminate the infinite loop

counter = 0
while(counter <= 10):
    print("value of :", counter, "is", counter)
    # only string can be concatenate not number
    # if you want to concatenate number then it must be converted to string by str(number_value)
    print("value of : " + str(counter) + " is " + str(counter))
    counter += 1