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


    def test_compare(self):
        self.assertEqual(self.c1.compare(self.c2),self.c2) # בדיקה האם הקלף הראשון שווה לאס והקלף השני לא, הפונקציה תחזיר את האס
        self.assertEqual(self.c2.compare(self.c1), self.c2) # בדיקה האם הקלף השני שווה לאס והראשון לא , הפונקציה תחזיר את האס
        self.assertEqual(self.c4.compare(self.c5), self.c4) # בדיקה כאשר הקלף הראשון שווה לקלף השני בערכו , הפונקציה תחזיר את הקלף שה-suit שלו גדול יותר
        self.assertEqual(self.c5.compare(self.c4), self.c4) # בודקת האם הפונקציה תחזיר את הקלף שה-suit שלו גדול יותר ללא תלות במי הקלף הראשון ומי השני
        self.assertEqual(self.c5.compare(self.c1),self.c1) # בודקת האם הפונקציה מחזירה את הקלף עם הערך הגדול יותר
        self.assertEqual(self.c1.compare(self.c5), self.c1) # בודקת האם הפונקציה מחזירה את הקלף עם הערך הגדול יותר ללא תלות במי הקלף הראשון ומי השני
        self.assertEqual(self.c2.compare(self.c6), self.c6) # בודקת שכאשר שני הקלפים שווים לAce הפונקציה תחזיר את הAce עם הsuit הגדול יותר
        # with self.assertRaises(AttributeError):
        #     self.c1.compare(self.c7)
        # self.assertEqual(self.c5.compare(self.c7), TypeError)





