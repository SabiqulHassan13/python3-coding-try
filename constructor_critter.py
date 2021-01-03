# -*- coding: utf-8 -*-
"""
Created on Tue Dec 25 23:33:27 2018

@author: Robin
"""
# Constructor Critter
# Demonstrates constructors

class Critter(object):
    """ A virtual Pet """
    def __init__(self):
        print("A new critter has been born!")
    def talk(self):
        print("\nHi, I'm an instance of class Critter.")
        
# main
def main():
    crit1 = Critter()
    crit1.talk()
    
    print()
    crit2 = Critter()
    crit2.talk() 

if __name__ == "__main__": main()