
# a. Modify the constructor, the withdraw and deposit methods in BankAccount such
# that if the amount is not supplied, a standard amount of 20 dollars is assumed.

class BankAccount:

    _interestRate = 0.03

    def __init__(self, id, amount=20):
        self._accountId = id
        self._balance = amount

    @property
    def accountId(self):
        return self._accountId

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, amt):
        self._balance = amt


    def deposit(self, amount=20):
        self._balance += amount
    
    def withdraw(self, amount=20):
        if amount <= self._balance:
            self._balance -= amount
            return True
        return False

    def transfer(self, ba, amount):
        if self.withdraw(amount):
            ba.deposit(amount)
            return True
        return False

    def accumulateInterest(self):
        self._balance += self._balance * type(self)._interestRate
    
    def __str__(self):
        return f'{self._accountId} {self._balance:.2f}'


class JuniorAccount(BankAccount):

    def __init__(self, id, balance, guardian):
        super().__init__(id, balance)
        self._guardian = guardian

# iii. Get property for guardian.

    @property
    def guardian(self):
        return self._guardian

# b. Modify the withdraw method in the JuniorAccount so that it does not limit the
# withdrawal provided the guardian is present with the junior account. The withdraw
# method has 2 parameters: the guardian’s name and the amount. Allow withdraw
# only if the guardian’s name parameter matches the instance variable guardian. It
# has the same return type as part iv of Question 1. If the guardian is present with
# the junior account holder, there is no withdrawal limit of 50 dollars

    def withdraw(self, amt, guardian=None): # same signature as method withdraw in the super class
        if guardian == self._guardian:
            super().withdraw(amt)
            return True
        elif amt <= 50: # limit only applies when guardian name does not match the so called guardian there
            super().withdraw(amt)
            return True
        else:
            return False

    def accumulateInterest(self):
        self._balance += self._balance * (type(self)._interestRate + 0.01)


# c. After modifying the withdraw method in part (b), discuss if any modification is
# required to the transfer method. In which class should we make the changes, if
# any.

    def transfer(self, ba, amount, guardian=None):
        if self.withdraw(amount, guardian):
            ba.deposit(amount)
            return True
        return False


    def __str__(self):
        return f"Guardian: {self.garudian} " + super().__str__()


if __name__ == "__main__":

    ba1 = BankAccount("001")
    ba2 = BankAccount("002", 100) # method overloading

    ja1 = JuniorAccount("003", 100, "Father")
    ja1.withdraw(80, "Mother")
    ja1.withdraw(80, guardian="Mother")
    ja1.withdraw(40)

    ja1.withdraw(60, "Father")

    ja1.deposit(100)
    ja1.transfer(ba1, 60)
    ja1.transfer(ba1, 60, "Father")

    print()