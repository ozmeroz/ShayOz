from GamesCards.DeckOfCards import *
from GamesCards.Card import *
class Player:
    'מחלקה המייצגת שחקן במשחק קלפים, לכל שחקן יש שם וחבילת קלפים. מספר הקלפים יקבע בעת תחילת משחק חדש ויהיה 10 כברירת מחדל'
    def __init__(self, mainpack,number_of_cards=10): # constructor
        self.mainpack=mainpack
        name=input("Enter name of player:")
        while not name.isalpha():
            name = input("This name is not valid , please enter a valid name: ")
        self.name=name
        self.playerPack=[]
        self.number_of_cards=number_of_cards


    def set_hand(self): # פונקציה שמחלקת חבילת קלפים חדשה ואקראית עבור השחקן
        self.playerPack = []
        if self.number_of_cards > 26: # בדיקה האם מספר הקלפים שהתקבל לשחקן גדול מ26, אם כן הגדרה של מספר הקלפים כ26 (מקסימום שהוגדר בפרוייקט)
            self.number_of_cards = 26
        for i in range(0, self.number_of_cards): # לולאה שמכניסה קלפים לחבילה של השחקן לפי מספר הקלפים שהוגדר
            self.playerPack.append(self.mainpack.deal_one())

    def get_card(self): # פונקציה שמושכת קלף אקראי מהשחקן והערך המוחזר שלה הוא הקלף שנמשך
        'במקרה שנמשך קלף משחקן בעל חפיסת קלפים ריקה מחזירה None'
        if(len(self.playerPack)<=0):
            return None
        else:
            i=randint(0,len(self.playerPack)-1) # הגרלה של אינדקס למשיכה מתוך רשימת הקלפים של השחקן
            card=self.playerPack.pop(i) # משיכת הקלף באינדקס שהוגרל
            return card


    def add_card(self, card): # פונקציה שמקבלת קלף ומוסיפה אותו לשחקן
        self.playerPack.append(card)

    def show(self): # פונקציה שמציגה את פרטי השחקן - שם וקלפים שיש בידו
        print(f"{self.name}: {self.playerPack}")