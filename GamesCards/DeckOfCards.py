from GamesCards.Card import *
from random import shuffle
from random import randint
class DecksOfCards:
    'מחלקה שמגדירה חפיסת קלפים'
    def __init__(self):
        self.pack=[]
        for i in range(1,5):
            for ind in range(1,14):
                c=Card(ind,i)
                self.pack.append(c)
        self.packShuffle()
        self.i=0 # משתנה עזר לפונקציה deal_one שנועד לצמצם טווח ערכים בהתאם להוצאת הקלפים מהחבילה המרכזית

    def packShuffle(self):
        shuffle(self.pack)

    # def deal_one(self):
    #     rndcard=randint(0,len(self.pack))
    #     chosenCard=self.pack.pop(rndcard)
    #     return chosenCard


    def deal_one(self):
        rndcard=randint(0,len(self.pack)-self.i)
        chosenCard=self.pack.pop(rndcard)
        self.i=self.i+1
        return chosenCard



    def show(self):
        for i in self.pack:
            print(i)






