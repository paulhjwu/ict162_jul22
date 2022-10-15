from datetime import datetime
from Flight_Passenger import Flight, Passenger
from Booking import *

class BookingException(Exception):
    '''Booking Exception User Defined Class'''

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

    def searchBooking(self, bookingId):
        return self.bookings.get(bookingId)

# The class has the following methods:
#  addBooking(booking) The method has a Booking object as parameter and adds the
# booking to the dictionary. The key is the booking id and the value the Booking object.
# The method returns True if the Booking object is added successfully and False
# otherwise.

# Revised requirement based on Lab4 Q3
#  addBooking(booking) - If the booking date (which is the current date) is
# after the Flight date, raise a BookingException with a message “Cannot
# book a past flight!”. Also raise a BookingException for duplicate booking,
# i.e. 2 bookings with same booking id.

    def addBooking(self, booking):
        if self.searchBooking(booking.bkid) is None:
            if booking.bkdate > booking.flight.departureDate:
                raise BookingException('Cannot book a past flight') 
            self._bookings[ booking.bkid ] = booking
        else:
            raise BookingException('Duplicate booking error')

#  changeBooking(bookingId, flight) Given a booking id and a flight, the method replaces
# the booking with another flight. Return True if the change is successful and False
# otherwise

# Revised

#  changeBooking(bookingId, flight) - The flight changed to must be later than
# booking date, otherwise raise a BookingException with an appropriate
# message. Also raise a BookingException if the bookingId is not found.

    def changeBooking(self, bookingId, newFlight):
        if self.searchBooking(bookingId) is not None:
            if newFlight.departureDate < self._bookings[bookingId].bkdate:
                raise BookingException(f'The flight changed to must be later than the booking date')
            self._bookings[bookingId].flight = newFlight
        else:
            raise BookingExcpetion(f"The {bookingId} is not found")

#  deleteBooking(bookingId) Given a booking id, the method removes the Booking from
# the dictionary if found. Return True if the remove is successful and False otherwise.

# Revised Requirements

#  deleteBooking(bookingId) - If the flight date is already past, booking
# cannot be removed. Raise a BookingException with an appropriate
# message. Also raise a BookingException for removing non-existing
# booking id.

    def deleteBooking(self, bookingId):
        booking = self.searchBooking(bookingId)
        if booking is not None:
            today = datetime.now()
            flightDate = booking.flight.departureDate
            if today > flightDate:
                raise BookingException('Cannot delete a past flight')
            self._bookings.pop(bookingId)
        else:
            raise BookingException('Removing non-existing booking id')



if __name__ == "__main__":

# Test the Airline class with the following statements:
# a. Create an Airline object.

    al1 = Airline('SQ')

    print()

# b. Add several bookings. To do this, create 3 Passenger objects, 

    p1 = Passenger("p1", "John", 1996)
    p2 = Passenger("p2", "Mary", 1997)
    p3 = Passenger("p3", "Steve", 2000)

# 3 Flight objects, 

    d1 = datetime(2022, 12, 25, 17, 30)
    f1 = Flight("SQ", "LA", d1, 2000)

    d2 = datetime(2022, 12, 25, 23, 15)
    f2 = Flight("SQ", "TK", d2, 1000)

    d3 = datetime(2022, 12, 26, 12, 15)
    f3 = Flight("SQ", "KL", d3, 300)

# 3 Booking objects 

    bkd = datetime.now()

    # bk1 = Booking(p1, f1, bkd)
    # bk2 = Booking(p2, f2, bkd)
    # bk3 = Booking(p3, f3, bkd)
    bk1 = IndividualBooking(p1, f1, bkd)
    bk2 = CorporateBooking(p2, f2, bkd, "SUSS")
    bk3 = IndividualBooking(p3, f3, bkd)

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
        if al1.searchBooking(bkid):
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

