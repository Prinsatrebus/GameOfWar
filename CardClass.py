#Define all card values to be used in deck

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')

values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

import random

game_on = True

at_war = False

#Create Class that will be used to define every card object in deck

class Card():
    
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
        
        
    def __str__(self):
        return self.rank + " of" + self.suit 
    
#Class that will be used to create and contain all card objects 

class Deck():
    
    def __init__(self):
        self.all_cards = []
        
        for suit in suits:
            for rank in ranks:
                
                # Create the Card object
                created_card = Card(suit, rank)
                
                self.all_cards.append(created_card)
                
        print('Successfully created deck')
                
    def shuffle(self):
        
        random.shuffle(self.all_cards)
        
    def deal_one(self):
        
        return self.all_cards.pop(0)
    
#Create Class that will be used to represent players and contain lists for player "hands"

class Player():
    
    def __init__(self, name):
        
        self.name = name
        self.all_cards = []
        
    def remove_one(self):
        
        return self.all_cards.pop(0)
        
    def add_cards(self,new_cards):
        
        if type(new_cards) == type([]):
            #for multiple card additions
            self.all_cards.extend(new_cards)
        else:
            #for single card additions
            self.all_cards.append(new_cards)
        
    def __str__(self):
        
        return f'Player {self.name} has {len(self.all_cards)} cards.'
        