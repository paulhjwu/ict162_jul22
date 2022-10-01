from Lab3_3 import MovieCard

# A HSBCMovieCard is also a MovieCard, but with more privileges for HSBC credit card
# holders. Card holders get 2 more tickets for the same prices. 

class HSBCMovieCard(MovieCard):

    _redeemLimit = 4

    def __init__(self, price, name):
        super().__init__(price)
        if price == 70 or price == 100:
            self._tickets += 2
        self._name = name

#Card holders are able to
# redeem up to a maximum of 4 tickets each time. 
# Write the HSBCMovieCard as a
# subclass of MovieCard with the following:

# a. A constructor that has the credit card holder name and the price. Card holders get 2
# more tickets, i.e. 12 for $70 and 17 for $100


# b. A redeemTicket method with qty as parameter. Default is 1. HSBCMovieCard
# holders can redeem up to 4 tickets at one time as long as there are tickets available
# in the card. If successful, it returns True, otherwise returns False.

## ==> We can reuse super class's redeemTicket, by declaring and overriding the class parameter _redeemLimit

# c. A __str__ method that returns the same information as the MovieCard, but with
# extra information of the name

    def __str__(self):
        return f"Name: {self._name} " + super().__str__()

if __name__ == "__main__":

    hmc1 = HSBCMovieCard(70, "John")
    hmc2 = HSBCMovieCard(100, "Peter")

    hmc1.redeemTicket(4)

    print(hmc1)
    print(hmc2)

    print()