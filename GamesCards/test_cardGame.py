from unittest import TestCase
from GamesCards.CardGame import CardGame
from GamesCards.Player import *

class TestCardGame(TestCase):


    def test___init__(self):
        cardGame = CardGame()
        cardGame2 = CardGame(20)
        self.assertEqual(cardGame.cards_to_player, 10) # בדיקה האם הערך הדיפולטיבי של מספר קלפים לשחקן עבד והוגדר כ10
        self.assertEqual(cardGame2.cards_to_player, 20) # בדיקה האם הערך של מספר קלפים לשחקן עבד כאשר התקבל כערך ביצירת משחק
        self.assertEqual(len(cardGame2.player1.playerPack), 20) # בדיקה האם נוצרה לשחקן חפיסת קלפים באורך שהתקבל בעת יצירת משחק


    def test_new_game(self):
        cardGame2 = CardGame(20)
        self.assertIsNone(cardGame2.new_game())  # בדיקה האם הפונקציה מחזירה none ולא ממשיכה כאשר נקראה לאחר שהמשחק כבר החל


    def test_get_winner(self):
        equalgame=CardGame(15) #    יצירת משחק חדש עם 2 שחקנים בלי מספר קלפים שווה
        self.assertIsNone(equalgame.get_winner()) #בדיקה האם הפונקציה החזירה None כמו שצריך כאשר יש תיקו
        card=equalgame.player1.get_card() # משיכת קלף משחקן ראשון
        equalgame.player2.add_card(card) # הכנסת הקלף לשחקן השני
        self.assertIs(equalgame.player1, equalgame.get_winner()) # בדיקה האם השחקן הראשון ניצח לאחר שהעברנו קלף שלו לשחקן השני
        card1=equalgame.player2.get_card() # לוקח קלף מהשחקן השני
        card2=equalgame.player2.get_card() # לוקח עוד קלף מהשחקן השני
        equalgame.player1.add_card(card1) # דוחף את הקלף לשחקן הראשון
        equalgame.player1.add_card(card2) # דוחף עוד קלף לשחקן הראשון כדי ליצור מצב שהשחקן השני מנצח ונכנסים לelse
        self.assertIs(equalgame.player2, equalgame.get_winner()) # בדיקה האם השחקן השני ניצח לאחר שהעברנו 2 קלפים שלו לשחקן הראשון

