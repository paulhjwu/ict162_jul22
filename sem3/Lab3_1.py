class BankAccount:

    _interestRate = 0.03

    def __init__(self, id, amount):
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

    def deposit(self, amount):
        self._balance += amount
    
    def withdraw(self, amount):
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

# Q1. a A JuniorAccount is a BankAccount. A JuniorAccount has an additional guardian
# as instance variable. Write the Junior Account class as follows:
# i. The JuniorAccount class as a subclass of BankAccount
# ii. A constructor that has the id, guardian and balance.

class JuniorAccount(BankAccount):

    def __init__(self, id, balance, guardian):
        super().__init__(id, balance)
        self._guardian = guardian

# iii. Get property for guardian.

    @property
    def guardian(self):
        return self._guardian

# iv. A withdraw method that limits withdrawal to maximum of 50 dollars. This
# method also returns true if the withdrawal is successful and false
# otherwise.

    def withdraw(self, amt): # same signature as method withdraw in the super class
        if amt <= 50:
            super().withdraw(amt)
            return True
        return False

# v. An accumulateInterest method that computes adds the interest amount to
# the balance. Junior account holders earn 1% more.

    def accumulateInterest(self):
        self._balance += self._balance * (type(self)._interestRate + 0.01)

# vi. The str method that returns all information of the junior account

    def __str__(self):
        return f"Guardian: {self.garudian} " + super().__str__()

if __name__ == "__main__":

    ba1 = BankAccount('001', 100)

# Q1.b Write an application to create a JuniorAccount object. Test the deposit,
# withdrawal and accumuateInterest methods.

    ja1 = JuniorAccount('002', 100, 'Father')

    ja1.deposit(100) # balance is 200

    ja1.accumulateInterest() # interest should 200 * 0.04 = 8

# c. Identify, where applicable, methods that exhibit method overriding by
# replacement/refinement

    print()