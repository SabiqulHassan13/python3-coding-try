# -*- coding: utf-8 -*-
"""
Created on Mon Dec 31 23:21:18 2018

@author: Robin
"""

# Instructions
# Demonstrates programmer-created functions

def instructions():
    """Display game instructions."""
    print(
    """
    Welcome to the greatest intellectual challange of all time: Tic-Tac-Toe.
    This will be a showdown between your human brain and my silicon processor.
    
    You will make your move known by entering a number. 0 - 8. 
    The number will correspond to the board position as illustrated:
    
        0 | 1 | 2
        ---------
        3 | 4 | 5
        ---------
        6 | 7 | 8
        
    Prepare yourself, human. The ultimate battle is about to begin.\n        
    """
    )
        
# main function
print("Here are the instructions to the Tic-Tac-Toe game: ")
instructions()
print("Here they are again: ")
instructions()
print("You probably understand the game by now.")

input("\n\nPress the enter key to exit.")