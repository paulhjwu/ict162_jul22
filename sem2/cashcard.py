class CashCard:
    #class variables
    __bonusAmount = 100
    __bonusRate = 0.01
    __running_number = 1

    #constructor
    # def __init__(self, id, value):
    #     self._id=id
    #     self._value=value
    def __init__(self, value=20):
        # running_number = 0
        self._id = CashCard.__running_number
        CashCard.__running_number += 1
        self._value=value
        #added in due to class variables
        if value >= type(self).__bonusAmount:
            self._value += self._value * type(self).__bonusRate
    
    #accessor
    @property
    def id(self):
        return self._id
    @property
    def value(self):
        return self._value

    def addBonus(self):
        if self._value >= type(self).__bonusAmount:
            self._value += value * type(self).__bonusRate
        
    #setter
    @value.setter
    def value(self, amount):
        self._value = amount
    
    # Behavior
    def topUp(self, amount):
        self._value += amount
        #added in due to class variables
        if self._value >= type(self).__bonusAmount:
            self._value += self._value * type(self).__bonusRate    

    def deduct(self, amount):
        if amount <= self._value:
            self._value -= amount
            return True
        else:
            return False
    
    def __str__(self):
        return f'Id: {self._id} value: {self._value}'

if __name__=="__main__":
    # c1 = CashCard(1, 100)
    # print(c1.value)
    # print(c1.id)
    
    # #testing of other behavior/method
    # c1.topUp(100)

    # print("After topUp 100", c1)

    # if c1.deduct(300):
    #     print(f"deduct is successful")
    # else:
    #     print(f"deduct fails")
    
    # print("After deduct 300", c1)

    # if c1.deduct(200):
    #     print(f"deduct is successful")
    # else:
    #     print(f"deduct fails")
    
    # print("After deduct 200", c1)

    # cashCards = []

    # c2 = CashCard(2, 300)
    # c3 = CashCard(3, 400)

    # cashCards.append(c1)
    # cashCards.append(c2)
    # cashCards.append(c3)

    # c4 = CashCard(4)
    # cashCards.append(c4)

    # c5 = CashCard(5, value=90) # == CashCard(5, 90)
    # cashCards.append(c5)

    # for x in cashCards:
    #     print(x)

    c1 = CashCard(100)
    c2 = CashCard(200)

    #add another cashcard
    c3 = CashCard(300)

    # # Consider collection of CashCard

    # aListOfStrings = []
    # aListOfStrings.append("a")
    # aListOfStrings.append("b")

    # cards = []
    # cards.append(c1)
    # cards.append(c2)

    # #cards.remove(c1)
    # #del cards[0]
    # #cards.pop(0)

    # print(aListOfStrings[0])
    # print(cards[0])

    # # https://www.w3schools.com/python/python_lists.asp 
    # # https://www.w3schools.com/python/python_lists_methods.asp

    # for i in cards:
    #     print(i)

    # for i in range(len(cards)):
    #     print(cards[i])

    # if c1 in cards:
    #     cards.remove(c1)

    # if c3 in cards:
    #     cards.remove(c3)

    # https://www.w3schools.com/python/python_dictionaries.asp
    # https://www.w3schools.com/python/python_dictionaries_loop.asp
    # https://www.w3schools.com/python/python_dictionaries_access.asp

    cards = {} # key, value pair 
    cards[c1.id] = c1
    cards[c2.id] = c2

    for c in cards:
        print(c)

    for c in cards.values():
        print(c)

    print(cards.get(c1.id))
    print(cards.get(c2.id))

    print()

