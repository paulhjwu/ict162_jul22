class CashCardException(Exception):
    ''' Exception class for exceptions raised in CashCard
    application '''

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
        if value < 0:
            raise CashCardException("Negative value, can't be created!")
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
            # return True
        else:
            # return False
            raise CashCardException("Not sufficient fund to be deducted")
    
    def __str__(self):
        return f'Id: {self._id} value: {self._value}'

if __name__ == "__main__":
    
    try:
        # CashCard(-100)
        c1 = CashCard(200)
        # if c1.deduct(100):
        #     print("Successful deduction")
        # else:
        #     print("Not successful deduction")
        c1.deduct(100)
        print("Deducted successfully")
    except CashCardException as e:
        print(e)
