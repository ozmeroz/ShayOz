from unittest import TestCase
from GamesCards.DeckOfCards import DecksOfCards

class TestDecksOfCards(TestCase):
    def setUp(self):
        self.d=DecksOfCards()


    def test___init___(self):
        self.assertEqual(len(self.d.pack),52)

    def test_packShuffle(self):
        self.fail()

    def test_deal_one(self):
        self.fail()

    def test_show(self):
        self.fail()
