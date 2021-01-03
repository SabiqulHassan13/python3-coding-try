# -*- coding: utf-8 -*-
"""
Created on Tue Dec 25 23:07:35 2018

@author: Robin
"""

# Simple Critter
# Demonstrate a basic class and object

class Critter(object):
    """A virtual pet"""
    def talk(self):
        print("Hi. I'm an instance of class Critter.")
        
# main
def main():
    crit = Critter()
    crit.talk()

if __name__ == "__main__": 
    main()