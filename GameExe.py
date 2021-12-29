import GameVariables
import time 

# Game Setup, create both players using Player class; new_deck is initial game deck that is shuffled and distributed into player_one/two.all_cards[] list

player_one = GameVariables.Player("One")
player_two = GameVariables.Player("Two")

game_start = input("Ready to play?")
game_start = game_start.upper()
if game_start == "Y" or "YES":
    game_on = True
    at_war = False
else:
    print('See you next time!')
    exit()

print()
print("Creating and shuffling deck...")
print()
time.sleep(2)
    
new_deck = GameVariables.Deck()
new_deck.shuffle()

# deal_one is method in Deck(new_deck) class where initial deck created is popped into each player's deck using add_cards method in Player class (append for single, extend for multiple)

print("Splitting deck into player stacks...")
print()
time.sleep(2)

for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())

# While Game On

game_board = []

while game_on:
    print()
    print(f'Player One has {len(player_one.all_cards)} remaining units in their army!')
    print()
    time.sleep(1)
    print(f'Player Two has {len(player_two.all_cards)} remaining units in their army!')
    print()
    time.sleep(2)
    fight_start = input('Start next fight?')
    print()
    fight_start = fight_start.upper()
    if fight_start != "Y" and fight_start != "YES":
        print()
        print("#1 The war has ended. See you next time!")
        print()
        exit()
    time.sleep(1)
    print('A fight has begun!')
    time.sleep(2)
    print()
    print(f'Player One has played {player_one.all_cards[0]}')
    print()
    time.sleep(1.5)
    print(f'Player Two has played {player_two.all_cards[0]}')
    print()
    
    time.sleep(1)
    
    if player_one.all_cards[0].value == player_two.all_cards[0].value:
        print()
        time.sleep(1)
        game_board.append(player_one.remove_one())
        game_board.append(player_two.remove_one())
        at_war = True
        print("The fight has escalated to a large battle!!")
        print()
        time.sleep(1)
        
    # While at war
    
        while at_war:
            fight_start = input('Continue this battle?')
            print()
            fight_start = fight_start.upper()
            if fight_start == "N" or fight_start == "NO":
                print('The war has ended. See you next time!')
                exit()
            print(f'Player One has sent their {player_one.all_cards[0]} into the battle!')
            print()
            time.sleep(2)
            print(f'Player Two has sent their {player_two.all_cards[0]} into the battle!')
            print()

            time.sleep(2)

            if player_one.all_cards[0].value > player_two.all_cards[0].value:
                print()
                print('Player One has won this battle!')
                print()
                time.sleep(2)
                game_board.append(player_one.remove_one())
                game_board.append(player_two.remove_one())
                player_one.add_cards(game_board)
                game_board = []
                at_war = False
                break
            elif player_one.all_cards[0] < player_two.all_cards[0]:
                print()
                print('Player Two has won this battle!')
                print()
                time.sleep(2)
                game_board.append(player_one.remove_one())
                game_board.append(player_two.remove_one())
                player_two.add_cards(game_board)
                game_board = []
                at_war = False
                break
            else:
                print()
                print('The battle continues!')
                print()
                time.sleep(1)
                game_board.append(player_one.remove_one())
                game_board.append(player_two.remove_one())
    elif player_one.all_cards[0].value > player_two.all_cards[0].value:
        print()
        print('Player One has won this fight!')
        print()
        time.sleep(2)
        game_board.append(player_one.remove_one())
        game_board.append(player_two.remove_one())
        player_one.add_cards(game_board)
        game_board = []
    else:
        print()
        print('Player Two has won this fight!')
        print()
        time.sleep(2)
        game_board.append(player_one.remove_one())
        game_board.append(player_two.remove_one())
        player_two.add_cards(game_board)
        game_board = []
    
    if len(player_one.all_cards) <= 0:
        print()
        print('Player Two has won the war!')
        print()
        time.sleep(2)
        game_on = False
    elif len(player_two.all_cards) <= 0:
        print()
        print('Player One has won the war!')
        print()
        time.sleep(2)
        game_on = False

print('Thanks for playing!')
