from GamesCards.DeckOfCards import *
from GamesCards.Card import *
class Player:
    'מחלקה המייצגת שחקן במשחק קלפים, לכל שחקן יש שם וחבילת קלפים. מספר הקלפים יקבע בעת תחילת משחק חדש ויהיה 10 כברירת מחדל'
    def __init__(self, mainpack, name,number_of_cards=10):
        self.mainpack=mainpack
        self.name=name
        self.playerPack=[]
        self.number_of_cards=number_of_cards


    def set_hand(self):
        self.playerPack = []
        if self.number_of_cards > 26:
            self.number_of_cards = 26
        for i in range(0, self.number_of_cards):
            self.playerPack.append(self.mainpack.deal_one())
    def get_card(self):
        i=randint(0,len(self.playerPack)-1)
        card=self.playerPack.pop(i)
        return card

    def add_card(self, card):
        self.playerPack.append(card)

    def show(self):
        print(f"{self.name}: {self.playerPack}")

