import GameVariables
import time 

# Game Setup, create both players using Player class; new_deck is initial game deck that is shuffled and distributed into player_one/two.all_cards[] list

player_one = GameVariables.Player("One")
player_two = GameVariables.Player("Two")

game_start = input("Ready to play?")
game_start = game_start.upper()
if game_start == "Y" or "Yes":
    game_on = True
    at_war = False
else exit()

print("Creating and shuffling deck...")
time.sleep(2)
    
new_deck = GameVariables.Deck()
new_deck.shuffle()

# deal_one is method in Deck(new_deck) class where initial deck created is popped into each player's deck using add_cards method in Player class (append for single, extend for multiple)

print("Splitting deck into player stacks...")
time.sleep(2)

for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())

# Verifying player object creation

for x in range(26):
    print(player_one.all_cards[x])
    
print(player_two)

# While Game On

game_board = []

while game_on:
    print(f'Player One has played {player_one.all_cards[0]')
    print(f'Player Two has played {player_two.all_cards[0]')
    
    game_board.append(player_one.all_cards.pop(0))
    game_board.append(player_two.all_cards.pop(0))
    
    time.sleep(1)
    
    if player_one.all_cards[0] = player_two.all_cards[0]:
        at_war = True
        print("A large battle has begun!!")
        while at_war = True:
            
    game_board.append()
    
    

# While at war