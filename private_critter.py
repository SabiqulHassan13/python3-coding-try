# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 17:59:57 2019

@author: Robin
"""

# Private Critter
# Demonstrates private variables and methods

class Critter(object):
    """A virtual pet"""
    def __init__(self, name, mood):
        print("A new critter has been born!")
        self.name = name    # public attribute
        self.__mood = mood  # private attribute
        
    def talk(self):
        print("\nI'm", self.name)
        print("Right now I feel", self.__mood, "\n")
     
    def __private_method(self):
        print("This is a private method.")
        
    def public_method(self):
        print("This is a public method.")
        self.__private_method()
        
def main():
    crit = Critter(name = "Poochie", mood = "happy")
    crit.talk()
    
    print(crit.name)
    # print(crit.__mood)        # it will print AttributeError
    print(crit._Critter__mood)  # it is correct but not encouraged to directly access private attribute
    
    crit.public_method()
    
if __name__ == "__main__": main()