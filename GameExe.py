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

# While Game On

game_board = []

while game_on:
    fight_start = input('Start next fight?')
    fight_start = fight_start.upper()
    if fight_start != "Y" and fight_start != "YES":
        print("#1 The war has ended. See you next time!")
        exit()
    print(f'Player One has played {player_one.all_cards[0]}')
    print(f'Player Two has played {player_two.all_cards[0]}')
    
    time.sleep(1)
    
    if player_one.all_cards[0] == player_two.all_cards[0]:
        print('A fight has begun!')
        game_board.append(player_one.deal_one())
        game_board.append(player_two.deal_one())
        at_war = True
        print("The fight has escalated to a large battle!!")
        while at_war:
            fight_start = input('Continue this battle?')
            fight_start = fight_start.upper()
            if fight_start == "N" or "NO":
                print('The war has ended. See you next time!')
                exit()
            print(f'Player One has sent their {player_one.all_cards[0]} into the battle!')
            time.sleep(2)
            print(f'Player Two has sent their {player_two.all_cards[0]} into the battle!')

            time.sleep(2)

            if player_one.all_cards[0].value > player_two.all_cards[0].value:
                print('Player One has won this battle!')
                game_board.append(player_one.deal_one())
                game_board.append(player_two.deal_one())
                player_one.add_cards(game_board)
                game_board = []
                at_war = False
                break
            elif player_one.all_cards[0] < player_two.all_cards[0]:
                print('Player Two has won this battle!')
                game_board.append(player_one.deal_one())
                game_board.append(player_two.deal_one())
                player_two.add_cards(game_board)
                game_board = []
                at_war = False
                break
            else:
                print('The battle continues!')
                game_board.append(player_one.deal_one())
                game_board.append(player_two.deal_one())
    elif player_one.all_cards[0] > player_two.all_cards[0]:
        print('Player One has won this fight!')
        game_board.append(player_one.deal_one())
        game_board.append(player_two.deal_one())
        player_one.add_cards(game_board)
        game_board = []
    else:
        print('Player Two has won this fight!')
        game_board.append(player_one.deal_one())
        game_board.append(player_two.deal_one())
        player_two.add_cards(game_board)
        game_board = []
    
    if len(player_one.all_cards) <= 0:
        print('Player Two has won the war!')
        game_on = False
    elif len(player_two.all_cards) <= 0:
        print('Player One has won the war!')
        game_on = False

print('Thanks for playing!')
