import random

class Dice:
    #class variable # of sides
    __sides = 6

    #accessor to class variable
    @classmethod
    def getSides(cls):
        return cls.__sides
    
    @classmethod
    def setSides(cls, sides):
        cls.__sides = sides

    #constructor
    def __init__(self):
        # self._value = random.randint(1,6)
        self._value = random.randint(1,type(self).getSides())

    #accessor
    @property
    def getValue(self):
        return self._value

    #behavior
    def roll(self):
        #self._value = random.randint(1,6)
        self._value = random.randint(1,type(self).getSides())

if __name__ == "__main__":
    d1 = Dice()
    print(d1.getValue)
    d1.roll()
    print(d1.getValue)

    Dice.setSides(50)
    d2 = Dice()
    print(d2.getValue)
    d2.roll()
    print(d2.getValue)

