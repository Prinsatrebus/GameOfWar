# GameOfWar
This is my 2nd milestone project in my python learning course. It is a digital version of the card game War. 

The game is played by shuffling a 52 card deck and splitting it into two 26 card stacks, one for each of the two players. Every round, each player removes the top card of their stack (or army) and plays it. Whoever wins the fight by having the higher rank card gets to add both of the played cards to the bottom of their stack. If both cards happen to be equal in rank, the fight then escalates to a war (or a large battle using in game dialogue) where both players continue playing the top card of their decks until one player wins by having the higher rank card. Upon winning the large battle, the winning player adds all of the cards that were played in that large battle to the bottom of their stack. The game ends when one player runs out of cards in their stack and is no longer able to play anything.

This game has three files:

GameVariables.py which contains most of the variables, classes, and methods that define all of the objects in the game

GameExe.py which contains the execution file with all of the game logic

__init__.py which allows for the import of GameVariables.py into GameExe.py upon execution of the GameExe.py file
