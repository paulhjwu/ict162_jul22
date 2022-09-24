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

    def __init__(self, ppNo, name, flight):
        self._ppNo = ppNo
        self._name = name
        self._flight = flight
    
    @property
    def flight(self):
        return self._flight
    
    def __str__(self):
        return f'ppNo: {self._ppNo}, name: {self._name}, flight: {self._flight}'

            
if __name__ == "__main__":

    # https://www.w3schools.com/python/python_datetime.asp 

    # a. Write the Passenger class.
    # b. Write an application to test the classes above by doing the following:
    # i. Create a Flight object f1 – SQ1 to LA on 25/12/2021 0415

    date1 = datetime(2021, 12, 25)
    f1 = Flight('SQ1', 'LA', date1 )

    # ii. Create a Passenger object p1 John, pp1 taking flight f1

    p1 = Passenger("pp1", "John", f1)

    # iii. Print the departure date for p1

    print(f'{p1.flight.departureDate:%d/%m/%Y %H:%M}')

    # iv. Create a Passenger object p2 also taking flight f1

    p2 = Passenger("pp2", "Mary", f1)

    # v. Print both passengers’ information using the str method

    print(p1)
    print(p2)

    # vi. Change the flight object’s departure date to 26/12/2021 1525

    d2 = datetime(2021, 12, 26, 15, 25)
    f1.departureDate = d2

    # vii. Print both passengers’ information using the str method.

    print(p1)
    print(p2)

    # test 

    print()