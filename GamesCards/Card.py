class Card:
    # 1=ace , 2-10 = numbers , 11=jack,12=queen,13=king
    # 1=diamond , 2 = spade , 3= heart , 4=club
    def __init__(self,value,suit):
        self.value=value
        self.suit=suit


    def __eq__(self, other):
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

