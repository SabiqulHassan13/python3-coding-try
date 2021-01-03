# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 10:09:13 2018

@author: Robin
"""

# Mood Computer
# Demonstrates the elif clause

import random

print("I sense your energy. Your true emotions are coming across my screen.")
print("You are...")

mood = random.randint(1, 3)

if(mood == 1):
    # happy
    print(\
          """
          -----------
          |         |
          |  o   o  |
          |    <    |
          |  -   -  |
          |   - -   |
          |    -    |
          -----------
          """)
elif(mood == 2):
    # neutral
    print(\
          """
          -----------
          |         |
          |  o   o  |
          |    <    |
          |         |
          |  ------ |
          |         |
          -----------
          """)
elif(mood == 3):
    # sad
    print(\
          """
          -----------
          |         |
          |  o   o  |
          |    <    |
          |    -    |
          |   - -   |
          |  -   -  |
          -----------
          """)
else:
    print("Illegal mood value! (You must be in a really bad mood).")
    print("...today.")

    