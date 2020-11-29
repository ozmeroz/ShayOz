from GamesCards.Player import *
from GamesCards.DeckOfCards import *
from GamesCards.Card import *
class CardGame:
    def __init__(self, cards_to_player=10):
        self.mainPack=DecksOfCards()
        self.player1 = Player(self.mainPack, "Shay", cards_to_player)
        self.player2 = Player(self.mainPack, "Oz", cards_to_player)
        self.new_game()


    def new_game(self):
        if self.player1 or self.player2:
            print("Error - Game already started!")
            return
        self.mainPack.packShuffle()
        self.player1.set_hand()
        self.player2.set_hand()

    def get_winner(self):
        if len(self.player1.playerPack)==len(self.player2.playerPack):
            return None
        if len(self.player1.playerPack)<len(self.player2.playerPack):
            return self.player1
        else:
            return self.player2