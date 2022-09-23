from cashcard import CashCard

class Customer:

##  first constructor
#     def __init__(self, name, card):
#         self._name = name
#         self._card = card

    def __init__(self, name, value):
        self._name = name
        self._card = CashCard(value)
    
    @property
    def card(self):
        return self._card

    @card.setter
    def card(self, newCard):
        self._card = newCard
    
    def topUp(self, amt):
        self._card.topUp(amt)

if __name__ == "__main__":

    # Only for the 1st Constructor
    # cc1 = CashCard(100)
    # cust1 = Customer("John", cc1)
    # cc2 = CashCard()
    # cust2 = Customer("Mary", cc2)

    cust1 = Customer("John", 100)
    print(cust1.card)

    cc2 = CashCard()
    cust1.card = cc2

    print(cust1.card)

    cust1.topUp(100)

    

    print()

