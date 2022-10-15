from Flight_Passenger import Flight, Passenger
from datetime import datetime
from abc import ABC, abstractmethod

class Booking(ABC):

    _bkId = 1

    def __init__(self, p1, f1, bookingDate):
        self._passenger = p1
        self._flight = f1
        self._bkid = Booking._bkId
        self._bkdate = bookingDate
        Booking._bkId += 1
    
    @property
    def bkdate(self):
        return self._bkdate

    @property
    def flight(self):
        return self._flight

    @property
    def passenger(self):
        return self._passenger
    
    @flight.setter
    def flight(self, newFlight):
        self._flight = newFlight

    @property
    def bkid(self):
        return self._bkid

    @abstractmethod
    def ticketPrice(self):
        pass

    def __str__(self):
        return f"Booking Id: {self._bkid}, Booking Date:{self._bkdate:%d/%m/%Y %H:%M}, Passenger: {self._passenger}, Flight: {self._flight}"

#  The IndividualBooking class is also a Booking. No additional instance variable. The
# class implements the ticketPrice() method. For individual booking, the ticket price
# for juniors below 18 and seniors 60 and above are entitled to 20% discount as
# declared in the class variable. Return the ticket price.

class IndividualBooking(Booking):

    _discount = 0.2

    def __init__(self, p1, f1, bookingDate):
        super().__init__(p1, f1, bookingDate)

    def ticketPrice(self):
        age = datetime.now().year - self.passenger.yearBorn
        fare = self.flight.fare
        if age < 18 or age >= 60:
            fare -= fare * type(self)._discount # discount applied
            return fare
        return fare

#  The CorporateBooking class is also a Booking. It has the company name as
# additional instance variable. 
# All corporate bookings are entitled to 50% discount as
# indicated in the class variable. Return the ticket price

class CorporateBooking(Booking):

    _discount = 0.5

    def __init__(self, p1, f1, bookingDate, coy_name):
        super().__init__(p1, f1, bookingDate)
        self._coyName = coy_name

    def ticketPrice(self):
        fare = self.flight.fare
        fare -= fare * type(self)._discount # discount applied
        return fare

if __name__ == "__main__":

    # Create 2 Passenger objects p1 and p2.

    p1 = Passenger("p1", "John", 2005) # < 18
    p2 = Passenger("p2", "Mary", 1960) # >= 60
    p3 = Passenger("p2", "Mary", 1970) # no discount

    # iii. Create 2 Flight objects f1 and f2.

    d1 = datetime(2021, 12, 25, 15, 45)
    f1 = Flight("SQ1", "LA", d1, 2000)
    d2 = datetime(2021, 12, 26, 10, 30)
    f2 = Flight("SQ2", "SG", d2, 1000)

    bkdate = datetime.now()

    bk1 = IndividualBooking(p1, f1, bkdate)
    bk2 = IndividualBooking(p3, f1, bkdate)
    bk3 = CorporateBooking(p2, f2, bkdate, "SUSS")

    print(bk1.ticketPrice())
    print(bk2.ticketPrice())
    print(bk3.ticketPrice())