from GamesCards.DeckOfCards import *
from GamesCards.Card import *
class Player:
    def __init__(self, mainpack, name,number_of_cards=10):
        self.mainpack=mainpack
        self.name=name
        self.playerPack=[]
        self.set_hand()

    def set_hand(self):
        self.playerPack = []
        if self.number_of_cards > 26:
            self.number_of_cards = 26
        for i in range(0, self.number_of_cards):
            self.playerPack.append(self.mainpack.deal_one())
    def get_card(self):
        card=self.playerPack.deal_one()
        return card

    def add_card(self, card):
        self.playerPack.append(card)

    def show(self):
        print(f"{self.name}: {self.playerPack}")

