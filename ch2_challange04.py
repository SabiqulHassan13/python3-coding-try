# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 09:00:12 2018

@author: Robin
"""

base_price = float(input("Enter the base price of car:"))
tax_fee = base_price * 0.8
license_fee = base_price * 0.3

dealer_prep = float(input("Enter the dealer prep price:"))
dest_chrg = float(input("Enter the destination charge:"))

total_fee = base_price + tax_fee + license_fee + dealer_prep + dest_chrg
print("Total actual price of the car is:", total_fee)