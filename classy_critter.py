# -*- coding: utf-8 -*-
"""
Created on Wed Jan  2 18:19:08 2019

@author: Robin
"""

# Classy Critter
# Demostrates class attributes and static methods

class Critter(object):
    """A virtual pet"""
    total = 0
    
    @staticmethod
    def status():
        print("\nTotal number of critters is", Critter.total)
        
    def __init__(self, name):
        print("A critter has been born!")
        self.name = name
        Critter.total += 1
        print("No of Critter object is", Critter.total)
    
# main    
def main():
    print("Accessing the class attribute Critter.total: ", end = " ")
    print(Critter.total)
    
    print("\nCreating critters.")
    crit1 = Critter("critter 1")
    crit2 = Critter("critter 2")
    crit3 = Critter("critter 3")

    Critter.status()
    print("Accessing the class attribute Critter.total: ", end = " ")
    print(Critter.total)
    
    input("\nPress the enter key to exit.")
    
if __name__ == "__main__": main()