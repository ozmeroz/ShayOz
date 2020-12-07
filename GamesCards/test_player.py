from unittest import TestCase
from GamesCards.Player import Player
from GamesCards.DeckOfCards import DecksOfCards
class TestPlayer(TestCase):
    def setUp(self):
        self.deck=DecksOfCards()
        self.player1=Player(self.deck)


    def test__init__(self):
        self.assertEqual(len(self.deck.pack), 52)
        self.player1.set_hand()
        self.assertEqual(len(self.player1.playerPack), self.player1.number_of_cards)
        self.assertFalse(self.player1.name,123)










        # def __init__(self, mainpack, number_of_cards=10):  # constructor
        #     self.mainpack = mainpack
        #     name = input("Enter name of player:")
        #     while not name.isalpha():
        #         name = input("This name is not valid , please enter a valid name: ")
        #     self.name = name
        #     self.playerPack = []
        #     self.number_of_cards = number_of_cards

    def test_set_hand(self):
        self.fail()

    def test_get_card(self):
        self.fail()

    def test_add_card(self):
        self.fail()

    def test_show(self):
        self.fail()
