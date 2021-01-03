# -*- coding: utf-8 -*-
"""
Created on Wed Jan  2 17:08:52 2019

@author: Robin
"""

# Attribute Critter
# Demonstrates creating and accessing object attributes

class Critter(object):
    """A virtual pet"""
    def __init__(self, name):
        print("A new critter has been born!")
        self.name = name
        
    def __str__(self):
        rep = "Critter object\n"
        rep += "name: " + self.name + "\n"
        return rep
    
    def talk(self):
        print("Hi. I'm", self.name, "\n")
        
def main():
    crit1 = Critter("Poochie")
    crit1.talk()
    
    print("Printing crit1:")
    print(crit1)
    
    print("Directly accessing crit1.name:", end = " ")
    print(crit1.name)
    
    crit2 = Critter("Randolph")
    crit2.talk()

if __name__ == "__main__": main()