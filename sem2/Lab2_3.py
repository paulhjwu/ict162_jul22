from datetime import datetime
from Lab2_2 import Flight, Passenger, Booking

# The bookings are managed by an Airline class which consists of 2 instance variables, the
# airline name and a dictionary collection of bookings. 

class Airline:

    def __init__(self, name):
        self._name = name
        self._bookings = {}

    @property
    def bookings(self):
        return self._bookings

#  Search(bookingId) Given a booking id, the method returns the Booking object if
# found, and None otherwise.

# https://www.w3schools.com/python/python_ref_dictionary.asp

    def search(self, bookingId):
        return self.bookings.get(bookingId)

# The class has the following methods:
#  addBooking(booking) The method has a Booking object as parameter and adds the
# booking to the dictionary. The key is the booking id and the value the Booking object.
# The method returns True if the Booking object is added successfully and False
# otherwise.

    def addBooking(self, booking):
        if self.search(booking.bkid) is None:
            self._bookings[ booking.bkid ] = booking
            return True
        else:
            return False

#  changeBooking(bookingId, flight) Given a booking id and a flight, the method replaces
# the booking with another flight. Return True if the change is successful and False
# otherwise

    def changeBooking(self, bookingId, newFlight):
        if self.search(bookingId) is not None:
            self._bookings[bookingId].flight = newFlight
            return True
        else:
            return False

#  deleteBooking(bookingId) Given a booking id, the method removes the Booking from
# the dictionary if found. Return True if the remove is successful and False otherwise.

    def deleteBooking(self, bookingId):
        if self.search(bookingId) is not None:
            self._bookings.pop(bookingId)
            return True
        else:
            False


if __name__ == "__main__":

# Test the Airline class with the following statements:
# a. Create an Airline object.

    al1 = Airline('SQ')

    print()

# b. Add several bookings. To do this, create 3 Passenger objects, 

    p1 = Passenger("p1", "John")
    p2 = Passenger("p2", "Mary")
    p3 = Passenger("p3", "Steve")

# 3 Flight objects, 

    d1 = datetime(2022, 12, 25, 17, 30)
    f1 = Flight("SQ", "LA", d1)

    d2 = datetime(2022, 12, 25, 23, 15)
    f2 = Flight("SQ", "TK", d2)

    d3 = datetime(2022, 12, 26, 12, 15)
    f3 = Flight("SQ", "KL", d3)

# 3 Booking objects 

    bkd = datetime.now()

    bk1 = Booking(p1, f1, bkd)
    bk2 = Booking(p2, f2, bkd)
    bk3 = Booking(p3, f3, bkd)

# and add the bookings. 

    al1.addBooking(bk1)
    al1.addBooking(bk2)
    al1.addBooking(bk3)

    print()

# For each booking, print the booking id.

    for i in al1.bookings.keys():
        print(f"The booking id is {i}")

# c. Search for a booking based on the booking id and display the details if found.

    for bkid in range(1,5):
        if al1.search(bkid):
            print(al1.bookings[bkid])
        else:
            print(f"No such booking id: {bkid}")
        
    print()

# d. Change one of the bookings to another flight.

    bkid = 1
    if al1.changeBooking(1, f2):
        print(f"The change from {f1} to {f2} is successfull")
    else:
        print(f"The change was not successful")

    print()

# e. Remove one booking.

    bkid = 1
    if al1.deleteBooking(bkid):
        print(f"The delete of booking id: {bkid} was successful")
    else:
        print(f"The change was not successful")

    print()

# f. Print all the bookings.

    for booking in al1.bookings.values():
        print(booking)
 
    print()

