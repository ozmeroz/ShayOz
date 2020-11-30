from GamesCards.Player import *
from GamesCards.DeckOfCards import *
from GamesCards.Card import *
from GamesCards.CardGame import *

game=CardGame()
game.player1.show()
game.player2.show()
game.new_game()
for i in range(10):
    card1=game.player1.get_card()
    card2=game.player2.get_card()
    print(card1)
    print(card2)
    if card1.compare(card2)==card1:
        game.player2.add_card(card1)
        game.player2.add_card(card2)
        print(f"Winner: {game.player1.name}")
    else:
        game.player1.add_card(card1)
        game.player1.add_card(card2)
        print(f"Winner: {game.player2.name}")
game.player1.show()
game.player2.show()