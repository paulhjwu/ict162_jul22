from cashcard import CashCard

class MemberCashCard(CashCard):

    def __init__(self, org, amt):
        super().__init__(amt)
        self._org = org
        self._points = 0
    
    @property
    def org(self):
        return self._org
    
    @property
    def points(self):
        return self._points

    @points.setter
    def points(self, newPoints):
        self._points = newPoints

    def deduct(self, amt):
        if super().deduct(amt) :
            self._points += int(amt)
            return True
        return False

    # def topUp(self, amt):
    #     if super().topUp(amt) :
    #         self._points += int(amt)
    #         return True
    #     return False

    def redeemPoints(self, points):
        if points <= self.points:
            self.topUp(points/2)
            self.points -= points

    def __str__(self):
        return f"Org: {self.org}, Points: {self.points} " + super().__str__()

if __name__ == "__main__":

    cd1 = CashCard(90)
    mcd1 = MemberCashCard("SUSS", 90)

    cd1.deduct(10)
    mcd1.deduct(10)

    mcd1.redeemPoints(10)

    print(mcd1)

    print()



