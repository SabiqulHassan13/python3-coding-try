# -*- coding: utf-8 -*-
"""
Created on Wed Jan  2 12:46:18 2019

@author: Robin
"""

# Tic-Tac-Toe
# plays the game of tic-tac-toe against a human opponent

# global constants
X = "X"
O = "O"
EMPTY = "TIE"
NUM_SQUARES = 9

def display_instruct():
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

def ask_yes_no():
    """Ask a yes or no question."""
    response = None
    while response not in ("y", "n"):
        response = input(question).lower()
    return response

def ask_number():
    "Ask for a number within a range."""
    response = None
    while response not in range(low, high):
        response = int(input(question))
    return response

def pieces():
    """Determine if player or computer goes first."""
    go_first = ask_yes_no("Do you require the first move? (y/n): ")
    if go_first == "y":
        print("\nThen take the first move. You will need it.")
        human = X
        computer = O
    else:
        print("\nYour bravery will be your undoing... I will go first.")
        computer = X
        human = O
    return computer, human
    
def new_board():
    """Create new game board."""
    board = []
    for square in range(NUM_SQUARES):
        board.append(EMPTY)
    return board

def display_board():
    """Display game board on screen."""
    print("\t", board[0], "|", board[1], "|", board[2])
    print("\t", "..........")
    print("\t", board[3], "|", board[4], "|", board[5])
    print("\t", "..........")
    print("\t", board[6], "|", board[7], "|", board[8], "\n")
    
def legal_moves(board):
    """Create list of legal moves."""
    moves = []
    for square in range(NUM_SQUARES):
        if board[square] == EMPTY:
            moves.append(square)
    return moves


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    