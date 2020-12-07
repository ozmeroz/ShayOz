from GamesCards.Card import *
from random import shuffle
from random import randint
class DecksOfCards:
    'מחלקה שמגדירה חפיסת קלפים'
    def __init__(self): #constructor
        self.pack=[] # הגדרת חפיסה ריקה
        for i in range(1,5):  #לולאה שמגדירה suit לקלף
            for ind in range(1,14): # לולאה שמגדירה value לקלף
                c=Card(ind,i)
                self.pack.append(c) # הכנסת קלף לחפיסה
        self.packShuffle() # ערבוב list של חפיסת הקלפים


    def packShuffle(self): # פונקציה שמשתמשת בshuffel של פייתון ומערבבת את חפיסת הקלפים
        shuffle(self.pack)



    def deal_one(self): # פונקציה שמוציאה קלף מהחפיסה והערך המוחזר שלה הוא הקלף שנבחר
        rndcard=randint(0,len(self.pack)-1) # מגריל אינדקס בין אפס לאינדקס האחרון ברשימה
        chosenCard=self.pack.pop(rndcard)
        return chosenCard



    def show(self): # פונקציה שמדפיסה את כל הקלפים בחפיסה
        for i in self.pack:
            print(i)