class Card:
    'מחלקה המייצגת קלף במשחק קלפים'
    # 1=ace , 2-10 = numbers , 11=jack,12=queen,13=king
    # 1=diamond , 2 = spade , 3= heart , 4=club
    def __init__(self,value,suit): # יצירת consrtuctor לclass

            self.value=value
            self.suit=suit



    def compare(self,other):  #יצירת פונקציית compare אשר מטרתה להשוות בין שני קלפים ולהחזיר את הקלף הגדול ביותר
        if (self.value > 13 or self.value  < 1 or other.value > 13 or other.value < 1):
            return "The value is Invalid"
        if (self.suit > 4 or self.suit < 1 or other.suit>4 or other.suit<1):
            return "The suit is Invalid"
        if self.value == 1 and other.value != 1: #בדיקה האם הקלף הראשון שווה לAce והשני שונה מAce
            return self # אם כן,הפונקציה תחזיר את הקלף הראשון
        if self.value != 1 and other.value ==1 : # בודקת האם הקלף השני שווה לAce והראשון שונה מAce
            return other # אם כן,הפונקציה תחזיר את הקלף השני
        if self.value == other.value: # בודקת האם שני הקלפים שווים
            if self.suit>other.suit: # אם כן, בודקת האם suit של הקלף הראשון גדול מהsuit של הקלף השני
                return self # אם כן, הפונקציה תחזיר את הקלף הראשון
            else : # אם לא
                return other # הפונקציה תחזיר את הקלף השני
        if self.value > other.value: # בודקת האם הקלף הראשון גדול מהקלף השני
            return self # אם כן, הפונקציה תחזיר את הקלף הראשון
        else: # אם לא
            return other # הפונקציה תחזיר את הקלף השני

    def __repr__(self): #יצירת פונקצית הדפסה
        if self.value==13: # בדיקה האם הקלף שווה ל13
            v="K" # אם כן , הקלף יודפס כKing
        elif self.value==12: # בדיקה האם הקלף שווה ל12
            v="Q" # אם כן , הקלף יודפס כQueen
        elif self.value==11: # בדיקה האם הקלף שווה ל11
            v="J" # אם כן , הקלף יודפס כJack
        elif self.value==1: # בדיקה האם הקלף שווה ל1
            v="A" # אם כן , הקלף יודפס כAce
        else: # אם הקלף אינו שווה לאחד מהערכים הנ"ל
            v=str(self.value) # הקלף יודפב בערכו
        if self.suit==1:# בדיקה האם הsuit שווה ל1
            s="♦" # אם כן,הקלף יודפס כDiamond
        if self.suit==2:# בדיקה האם הsuit שווה ל2
            s = "♠" # אם כן,הקלף יודפס כSpade
        if self.suit==3:# בדיקה האם הsuit שווה ל3
            s="♥" # אם כן,הקלף יודפס כHeart
        if self.suit==4:# בדיקה האם הsuit שווה ל4
            s="♣" # אם כן,הקלף יודפס כClub
        return (f"{v}:{s}") # הדפסת הקלף לפי הערכים שנקבעו בפונקציה הנ"ל לפי משתנים v ן- s

