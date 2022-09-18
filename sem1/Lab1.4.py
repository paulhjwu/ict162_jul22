class BankAccount:
    
    def __init__(self, accountId:str, pin:int, balance:float=100):
        self._accountId = accountId
        self._pin = pin
        self._balance = balance

    @property
    def accountId(self):
        return self._accountId

    @property
    def pin(self):
        return self._pin
    
    @property
    def balance(self):
        return self._balance
    
    @balance.setter
    def balance(self, newBalance):
        self._balance = newBalance
    
    def changePin(self, oldPin, newPin):
        if oldPin == self.pin:
            self._pin = newPin
            return True
        else:
            return False

    def deposit(self, amount):
        self._balance += amount
    
    def withdraw(self, amount):
        if amount > self._balance:
            return False
        else:
            self._balance -= amount
            return True

    def transfer(self, toBankAccount, amount):
        if self.withdraw(amount):
            toBankAccount.deposit(amount)
            return True
        else:
            return False

    def __str__(self):
        return f"accountId: {self._accountId}, balance: {self._balance}"

if __name__ == "__main__":

#### Requirements ####

# A BankAccount class has 3 instance variables: accountId, pin and balance.
# It has a constructor that has 3 parameters to initialize the accountId, pin and
# the amount. The default balance is $100. It has getter properties for accountId
# pin, and balance. It has setter property for balance.

# It has the following methods:

#  A changePin method that has old pin and new pin as parameters. The new
# pin is updated only if the old pin matches the existing pin. Return true if the
# change is successful and false otherwise.

#  A deposit method with parameter amount which represents the amount to
# deposit. The method adds the amount to the balance.

#  A withdraw method with parameter amount which represents the withdrawal
# amount. This method deducts the amount from the balance and returns True
# if there is sufficient balance, and False otherwise.

#  A transfer method that has 2 parameters – another bank account to transfer
# to and the amount to transfer. The method returns True if the transfer is
# successful and False otherwise.

#  The __str__() method returns the accountId and balance as a string.

#### Testing #####

# Test out the BankAccount as follows:
# i. Declare a BankAccount object b1 for account ’B1’, pin 111, amount 100.

    b1 = BankAccount('B1', 111, 100.0)


# ii. Make a deposit of $100 for b1. Display the details of the account.

    b1.deposit(100)

    print()

# iii. Change the pin for b1. Display the outcome of the change.

    if b1.changePin(111, 120):
        print("The pin has been changed")
    else:
        print("Wrong pin")

    print()

# iv. Declare another BankAccount object b2 for account ’B2’, pin 222, amount
# 100.

    b2 = BankAccount('B2', 222, 100.0)

# v. Make a withdrawal amount of $200 for b2 and display whether the
# withdrawal is successful.

    if b2.withdraw(200):
        print("Withdraw is successful")
    else:
        print("Withdrawa is not successful")
    
    print()

# vi. Transfer $100 from bank account b1 to b2. Display whether the transfer is
# successful.

    if b1.transfer(b2, 100):
        print("The transfer is successful")
    else:
        print("The transfer is not successful")

    print()   

# vii. Display the bank balances of both accounts.

    print(b1)
    print(b2)