# A cinema sells movie cards. For $70, a movie goer can watch 10 movies and for $100,
# 15 movies. Write a MovieCard class that represents a movie card with the following:
# a. A constructor that has price as parameter to initialize the instance variable price.

# Assume that the parameter value will be 70, or 100. Another instance variable is
# used to store the number of tickets based on the price, i.e. self_tickets=10 or 15
# depending on the price.

class MovieCard:

    _redeemLimit = 2

    def __init__(self, price):
        self._price = price

        if price == 70:
            self._tickets = 10
        elif price == 100:
            self._tickets = 15
        else:
            self._tickets = 0
    
# b. A property tickets that returns the number of tickets remaining.

    @property
    def tickets(self):
        return self._tickets

# c. A redeemTicket method with qty as parameter. Default is 1. Each redemption is
# for maximum of 2 tickets only. If there are still tickets left, subtract the number of
# tickets and return True, otherwise return False.

    def redeemTicket(self, qty=1):
        if qty > type(self)._redeemLimit:
            return False
        elif qty < 0:
            return False
        else:
            self._tickets -= qty
            return True
        
# d. A __str__ method, that returns the price and the tickets remaining in this format:
# Ticket price: $70, tickets remaining: 2

    def __str__(self):
        return f"Ticket price: {self._price}, tickets remaining: {self._tickets}"

if __name__ == "__main__":

    mc1 = MovieCard(70)
    mc2 = MovieCard(100)
    mc3 = MovieCard(80)

    mc1.redeemTicket(3)
    mc1.redeemTicket(2)

    print(mc1)

    print()
# Test this class by creating a movie object and redeem some tickets. Print the tickets
# remaining.

