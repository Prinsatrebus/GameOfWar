#Define all card values to be used in deck

Suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
Ranks = ('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')

Values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

import random

playing = True

#Create Class that will be used to define every card object in deck

class Card():
    
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        
        
    def __str__(self):
        return self.rank + " of" + self.suit 
    
#Create Class that will be used to contain all card objects 

class Deck():
    
    def __init__(self):
        self.deck = []
        