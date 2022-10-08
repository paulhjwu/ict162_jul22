from datetime import datetime

class Flight:
    def __init__(self, flightNo, destination, departureDate):
        self._flightNo = flightNo
        self._destination =destination
        self._departureDate = departureDate

    @property
    def flightNo(self):
        return self._flightNo

    @property
    def destination(self):
        return self._destination

    @property
    def departureDate (self):
        return self._departureDate
    
    @flightNo.setter
    def flightNo(self, flightNo):
        self._flightNo = flightNo
   
    @departureDate.setter
    def departureDate (self, departureDate):
        self._departureDate = departureDate
    
    def __str__(self):
        return f'Flight: {self._flightNo} Destination: {self._destination} Departure \
            Date: {self._departureDate:%d/%m/%Y %H:%M }'

    # Use composition to write a Passenger class. It has 3 instance variables – ppNo (str),
    # name(str) and flight(Flight).

class Passenger:

    # def __init__(self, ppNo, name, flight):
    def __init__(self, ppNo, name):
        self._ppNo = ppNo
        self._name = name
        # self._flight = flight
    
    @property
    def flight(self):
        return self._flight
    
    def __str__(self):
        # return f'ppNo: {self._ppNo}, name: {self._name}, flight: {self._flight}'
        return f'ppNo: {self._ppNo}, name: {self._name}'

# A Booking class is introduced to store Passenger and Flight booking. The class has 3
# instance variables, the booking id which starts from the class variable bkNum=1 and
# increments by 1 for every new booking, a passenger and flight. It has properties for
# booking id, passenger and flight, and flight setter to allow change of flight. The str()
# method displays the booking details as follows:
# Booking id: 1
# Passport No: PP1 Name: John
# Flight: SQ1 Destination: LA Departure Date: 25/12/2021 04: 

class Booking:

    _bkId = 1

    def __init__(self, p1, f1, bookingDate):
        self._passenger = p1
        self._flight = f1
        self._bkid = Booking._bkId
        self._bkdate = bookingDate
        Booking._bkId += 1
    
    @property
    def flight(self):
        return self._flight

    @property
    def bkdate(self):
        return self._bkdate

    @flight.setter
    def flight(self, newFlight):
        self._flight = newFlight

    @property
    def bkid(self):
        return self._bkid

    def __str__(self):
        return f"Booking Id: {self._bkid}, Booking Date:{self._bkdate:%d/%m/%Y %H:%M}, Passenger: {self._passenger}, Flight: {self._flight}"

if __name__ == "__main__":

    # Write the Booking class.
    # Test the class with the following statements:
    # i. Create an empty list to store booking objects.

    bookings = []

    # ii. Create 2 Passenger objects p1 and p2.

    p1 = Passenger("p1", "John")
    p2 = Passenger("p2", "Mary")

    # iii. Create 2 Flight objects f1 and f2.

    d1 = datetime(2021, 12, 25, 15, 45)
    f1 = Flight("SQ1", "LA", d1)
    d2 = datetime(2021, 12, 26, 10, 30)
    f2 = Flight("SQ2", "SG", d2)

    # iv. Create 2 booking objects for the passengers and flights created and add to the list,
    # p1 taking f1 and p2 taking f2.

    bkdate = datetime.now()

    bk1 = Booking(p1, f1, bkdate)
    bk2 = Booking(p2, f2, bkdate)
    bookings.append(bk1)
    bookings.append(bk2)

    # v. Display the details of the bookings from the list.

    for bk in bookings:
        print(bk)

    # vi. Make changes such that both passengers are taking the same f1 flight.

    bk2.flight = f1

    # vii. Display the details of the booking.

    for bk in bookings:
        print(bk)

    # viii. Change the flight departure date for the flight that both passengers are taking.

    d3 = datetime(2021, 12, 26, 18, 0)
    f1.departureDate = d3

    # ix. Display the details of the booking again.

    for bk in bookings:
        print(bk)

    print()