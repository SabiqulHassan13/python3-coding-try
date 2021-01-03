# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 18:26:15 2018

@author: Robin
"""

# Quotation manipulation
# Demonstrate string methods

# Quote from IBM Chairman, Thomas Watson, in 1943
quote = " I think there is a world market for maybe five computers. "

print("Original Quote:")
print(quote)

print("In Uppercase:")
print(quote.upper())

print("In Lowercase:")
print(quote.lower())

print("In Swapcase:")
print(quote.swapcase())

print("In Capitalized:")
print(quote.capitalize())

print("In Strip:")
print(quote.strip())

print("As a title:")
print(quote.title())

print("With a minor replacement:")
print(quote.replace("five", "millions of"))

print("Original quote is still:")
print(quote)

input("Press the enter key to exit.")