from GamesCards.Player import *
from GamesCards.DeckOfCards import *
from GamesCards.Card import *
class CardGame:
    'מחלקה המייצגת משחק, כוללת חפיסת קלפים אחת ושני שחקנים'
    def __init__(self, cards_to_player=10): #constructor, מקבל כפרמטר את מספר הקלפים שיש לחלק לכל שחקן, 10 כברירת מחדל, ויוצר חפיסת קלפים חדשה למשחק
        self.mainPack=DecksOfCards()
        self.cards_to_player=cards_to_player

        self.player1 = Player(self.mainPack, self.cards_to_player)
        self.player2 = Player(self.mainPack, self.cards_to_player)
        self.new_game()



    def new_game(self):
        'מתודה שתערבב את החפיסה מחדש ומחלקת קלפים לשחקנים. אם המתודה תיקרא מסיבה כל שהיא לאחר שהמשחק החל היא מדפיסה הודעה שהמשחק כבר החל ולא עושה כלום'
        if self.player1.playerPack!=[]: # בדיקה האם המשחק כבר החל והפונקציה נקראה לא במקום
            print("Game already started!")
            return None
        self.mainPack.packShuffle() # ערבוב החפיסה הראשית
        self.player1.set_hand() #קריאה לפונקציה שמחלקת חבילת קלפים לשחקן הראשון
        self.player2.set_hand() # קריאה לפונקציה שמחלקת חבילת קלפים לשחקן השני


    def get_winner(self):
        'פונקציה שבודקת מי השחקן המנצח ומחזירה אותו'
        if len(self.player1.playerPack)==len(self.player2.playerPack): # בדיקה אם מספר הקלפים בחפיסה של שני השחקנים שווה
            return None
        if len(self.player1.playerPack)<len(self.player2.playerPack): #בדיקה מי המנצח והחזרה של השחקן המנצח
            return self.player1
        else:
            return self.player2