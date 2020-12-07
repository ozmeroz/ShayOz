from GamesCards.Player import *
from GamesCards.DeckOfCards import *
from GamesCards.Card import *
from GamesCards.CardGame import *
import time

game=CardGame()
game.player1.show() #הדפסת שחקן
game.player2.show() #הדפסת שחקן
game.new_game() # בדיקת קריאה לפונקציה new_game לאחר שהמשחק כבר החל
for i in range(10):
    card1=game.player1.get_card()
    card2=game.player2.get_card()
    print(f"{game.player1.name}-{card1}")
    print(f"{game.player2.name}-{card2}")
    if card1.compare(card2)==card1:
        game.player2.add_card(card1)
        game.player2.add_card(card2)
        print(f"This round Winner is : {game.player1.name}\n")
    else:
        game.player1.add_card(card1)
        game.player1.add_card(card2)
        print(f"This round Winner is : {game.player2.name}\n")
    time.sleep(2)
game.player1.show()
game.player2.show()
if game.get_winner()!=None:
    print(f"The winner is : {game.get_winner().name}!!!")
else:
    print("There is no Winners, Just loosers! \nThe game ended in draw!")
