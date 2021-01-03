# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 13:40:35 2019

@author: Robin
"""

# Alien Blaster
# Demonstrates object interaction

class Player(object):
    """A player in a shooter game."""
    def blast(self, enemy):
        print("The player blasts an enemy.\n")
        enemy.die()
        
class Alien(object):
    """An alien in a shooter game."""
    def die(self):
        print("The alien gasps and says, 'Oh, this is it. This is the big one.\n" \
              "Yes, it's getting dark now. Tell my 1.6 million larvae that I love them... \n" \
              "Good-bye, cruel universe.'")
        
def main():
    print("\t\tDeath of an Alien\n")
    
    hero = Player()
    invader = Alien()
    hero.blast(invader)    
    
if __name__ == "__main__": main()