class CashCard (object):
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
 
    c1 = CashCard(100)

    print(c1)
    print(id(c1))