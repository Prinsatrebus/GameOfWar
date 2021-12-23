import GameVariables

# Game Setup, create both players using Player class; new_deck is initial game deck that is shuffled and distributed into player_one/two.all_cards[] list

player_one = GameVariables.Player("One")
player_two = GameVariables.Player("Two")

new_deck = GameVariables.Deck()
new_deck.shuffle()

# deal_one is method in Deck(new_deck) class where initial deck created is popped into each player's deck using add_cards method in Player class (append for single, extend for multiple)

for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())

# Verifying player object creation

for x in range(26):
    print(player_one.all_cards[x])
    
print(player_two)

# While Game On

# While at war