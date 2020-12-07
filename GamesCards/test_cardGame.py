from unittest import TestCase
from GamesCards.CardGame import CardGame
from GamesCards.Player import *

class TestCardGame(TestCase):

    def setUp(self):
        self.cardGame = CardGame()
        self.cardGame2 = CardGame(20)
        self.equalgame= CardGame(15)


    def test___init__(self):

        self.assertEqual(self.cardGame.cards_to_player, 10) # בדיקה האם הערך הדיפולטיבי של מספר קלפים לשחקן עבד והוגדר כ10
        self.assertEqual(self.cardGame2.cards_to_player, 20) # בדיקה האם הערך של מספר קלפים לשחקן עבד כאשר התקבל כערך ביצירת משחק
        self.assertEqual(len(self.cardGame2.player1.playerPack), 20) # בדיקה האם נוצרה לשחקן חפיסת קלפים באורך שהתקבל בעת יצירת משחק


    def test_new_game(self):
        self.assertIsNone(self.cardGame2.new_game())  # בדיקה האם הפונקציה מחזירה none ולא ממשיכה כאשר נקראה לאחר שהמשחק כבר החל


    def test_get_winner(self):
         #    יצירת משחק חדש עם 2 שחקנים בלי מספר קלפים שווה
        self.assertIsNone(self.equalgame.get_winner()) #בדיקה האם הפונקציה החזירה None כמו שצריך כאשר יש תיקו
        card=self.equalgame.player1.get_card() # משיכת קלף משחקן ראשון
        self.equalgame.player2.add_card(card) # הכנסת הקלף לשחקן השני
        self.assertIs(self.equalgame.player1, self.equalgame.get_winner()) # בדיקה האם השחקן הראשון ניצח לאחר שהעברנו קלף שלו לשחקן השני
        card1=self.equalgame.player2.get_card() # לוקח קלף מהשחקן השני
        card2=self.equalgame.player2.get_card() # לוקח עוד קלף מהשחקן השני
        self.equalgame.player1.add_card(card1) # דוחף את הקלף לשחקן הראשון
        self.equalgame.player1.add_card(card2) # דוחף עוד קלף לשחקן הראשון כדי ליצור מצב שהשחקן השני מנצח ונכנסים לelse
        self.assertIs(self.equalgame.player2, self.equalgame.get_winner()) # בדיקה האם השחקן השני ניצח לאחר שהעברנו 2 קלפים שלו לשחקן הראשון

