class Card:
    'מחלקה המייצגת קלף במשחק קלפים'
    # 1=ace , 2-10 = numbers , 11=jack,12=queen,13=king
    # 1=diamond , 2 = spade , 3= heart , 4=club
    def __init__(self,value,suit):
        self.value=value
        self.suit=suit


    # def __eq__(self, other):
    def compare(self,other):
        if self.value==1 and other.value != 1:
            return self
        if self.value != 1 and other.value ==1 :
            return other
        if self.value == other.value:
            if self.suit>other.suit:
                return self
            else :
                return other
        if self.value > other.value:
            return self
        else:
            return other

    def __repr__(self):
        if self.value==13:
            v="King"
        elif self.value==12:
            v="Queen"
        elif self.value==11:
            v="Jack"
        elif self.value==1:
            v="Ace"
        else:
            v=str(self.value)
        if self.suit==1:
            s="Diamond"
        if self.suit==2:
            s = "Spade"
        if self.suit==3:
            s="Heart"
        if self.suit==4:
            s="Club"
        return (f"{v}:{s}")

