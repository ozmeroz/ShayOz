from unittest import TestCase
from GamesCards.DeckOfCards import DecksOfCards
from GamesCards.Card import Card
class TestDecksOfCards(TestCase):
    def setUp(self):
        self.d=DecksOfCards()
        self.c=Card(1,1)


    def test___init___(self):
        self.assertEqual(len(self.d.pack),52) #     בדיקה האם הפונקציה איתחלה חפיסת קלפים באורך 52 כמספר הקלפים שיש במשחק


    def test_packShuffle(self):
        check=self.d.pack[0] #משיכת הקלף הראשון בחבילה
        self.d.packShuffle() #ערבוב החבילה
        check2=self.d.pack[0] #משיכת הקלף הראשון לצורך בדיקה האם החבילה עורבבה
        self.assertNotEqual(check, check2)

    def test_deal_one(self):
        self.d.deal_one() # הוצאה של קלף מהחבילה
        self.assertEqual(len(self.d.pack), 51) # בדיקה האם אורך הליסט קטן לאחר הוצאה של קלף

