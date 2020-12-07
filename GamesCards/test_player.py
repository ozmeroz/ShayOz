from unittest import TestCase
import GamesCards
from GamesCards.Player import Player
from GamesCards.DeckOfCards import DecksOfCards
from GamesCards.Card import Card
from unittest import mock
class TestPlayer(TestCase):
    def setUp(self):
        self.deck=DecksOfCards()
        self.player1=Player(self.deck,30)


    def test__init__(self):
        self.assertEqual(len(self.deck.pack), 52) # בדיקה האם החפיסה של המשחק מלאה בכל הקלפים
        self.assertIs(len(self.player1.playerPack), 0) # בדיקה האם החפיסה של השחקן ריקה
        self.player1.set_hand() # הכנסת קלפים לחפיסה של השחקן
        self.assertEqual(len(self.player1.playerPack), self.player1.number_of_cards) # בדיקה האם גודל החבילה של השחקן שווה למספר שהוגדר בעת יצירת השחקן


    @mock.patch('GamesCards.DeckOfCards.DecksOfCards.deal_one', return_value=Card(1,1))
    def test_set_hand(self,mocked_dealone):
        self.assertIs(len(self.player1.playerPack), 0)  # בדיקה האם החפיסה של השחקן ריקה
        self.player1.set_hand() # הכנסת קלפים לחפיסה של שחקן שיצרנו עם 30 קלפים למרות שהמקסימום הוא 26
        self.assertEqual(self.player1.number_of_cards,26)# בדיקה האם הפונקציה set_hand נתנה לשחקן 26 קלפים כמו שצריך במקרה והוא מקבל כפרמטר מספר גדול יותר מהמקסימום
        self.player1.playerPack.append(mocked_dealone) # שימוש במוק על מנת לדמות שימוש בפונקציה deal_one ללא תלות בפונקציה המקורית
        self.assertIn(mocked_dealone,self.player1.playerPack)


    def test_get_card(self):
        self.assertIsNone(self.player1.get_card()) # קריאה לפונקציה ובדיקה האם היא מחזירה None כאשר אין לשחקן קלפים
        self.player1.set_hand() # חלוקת קלפים לשחקן
        newPlayer=Player(self.deck) # יצירת שחקן חדש בלי קלפים
        newcard=Card(10,2) # הכנה של קלף יחיד לצורך בדיקה
        newPlayer.add_card(newcard) #הכנסה של קלף יחיד לשחקן
        self.assertIs(newPlayer.get_card(), newcard) #בדיקה האם הקלף שנמשך הוא הקלף שהכנסו


    def test_add_card(self):
        newcard=Card(7,3)
        self.player1.add_card(newcard)
        self.assertIs(newcard,self.player1.playerPack[len(self.player1.playerPack)-1])
