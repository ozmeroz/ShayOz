from unittest import TestCase
from GamesCards.Card import Card


class TestCard(TestCase):

    def setUp(self) :
        self.c1=Card(12,2)
        self.c2=Card(1,3)
        self.c3=Card(7,1)
        self.c4=Card(5,4)
        self.c5=Card(5,2)
        self.c6=Card(1,4)
        self.c7=Card(15,2)
        self.c8=Card(10,6)


    def test_compare_invalid(self):
        self.assertIn("Invalid",self.c7.compare(self.c6))
        self.assertIn("Invalid", self.c6.compare(self.c7))
        self.assertIn("Invalid", self.c8.compare(self.c6))
        self.assertIn("Invalid", self.c6.compare(self.c8))

    def test_compare_Ace(self):
        self.assertEqual(self.c1.compare(self.c2),self.c2) # בדיקה האם הקלף הראשון שווה לאס והקלף השני לא, הפונקציה תחזיר את האס
        self.assertEqual(self.c2.compare(self.c1), self.c2) # # בדיקה האם הקלף השני שווה לאס והראשון לא , הפונקציה תחזיר את האס

    def test_compare_evenButSuitIsBigger(self):
        self.assertEqual(self.c4.compare(self.c5), self.c4) # בדיקה כאשר הקלף הראשון שווה לקלף השני בערכו , הפונקציה תחזיר את הקלף שה-suit שלו גדול יותר
        self.assertEqual(self.c5.compare(self.c4), self.c4) # בודקת האם הפונקציה תחזיר את הקלף שה-suit שלו גדול יותר ללא תלות במי הקלף הראשון ומי השני

    def test_compare_biggerValue(self):
        self.assertEqual(self.c5.compare(self.c1),self.c1) # בודקת האם הפונקציה מחזירה את הקלף עם הערך הגדול יותר
        self.assertEqual(self.c1.compare(self.c5), self.c1) # בודקת האם הפונקציה מחזירה את הקלף עם הערך הגדול יותר ללא תלות במי הקלף הראשון ומי השני

    def test_compare_AceAndSuit(self):
        self.assertEqual(self.c2.compare(self.c6), self.c6) # בודקת שכאשר שני הקלפים שווים לAce הפונקציה תחזיר את הAce עם הsuit הגדול יותר











