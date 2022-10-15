from datetime import datetime

#  Flight class – additional instance variable fare and property for fare.

class Flight:
    def __init__(self, flightNo, destination, departureDate, fare):
        self._flightNo = flightNo
        self._destination =destination
        self._departureDate = departureDate
        self._fare = fare # added

    @property # added
    def fare(self):
        return self._fare

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

# Passenger class – additional instance variable yearBorn and property for yearBorn
   
    def __init__(self, ppNo, name, yearBorn):
        self._ppNo = ppNo
        self._name = name
        self._yearBorn = yearBorn # added
        # self._flight = flight
    
    @property  # added
    def yearBorn(self):
        return self._yearBorn
    
    def __str__(self):
        # return f'ppNo: {self._ppNo}, name: {self._name}, flight: {self._flight}'
        return f'ppNo: {self._ppNo}, name: {self._name}'

#  The Booking class is an abstract class. 
# Other additional instance variable includes
# the bookingDate and property for bookingDate. 
# It has an abstract method ticketPrice() which currently has no implementation

