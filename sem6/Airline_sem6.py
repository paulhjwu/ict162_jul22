from datetime import datetime
from Flight_Passenger_sem6 import Flight, Passenger
from Booking_sem6 import *

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
            raise BookingException(f"The {bookingId} is not found")

#  deleteBooking(bookingId) Given a booking id, the method removes the Booking from
# the dictionary if found. Return True if the remove is successful and False otherwise.

# Revised Requirements

#  deleteBooking(bookingId) - If the flight date is already past, booking
# cannot be removed. Raise a BookingException with an appropriate
# message. Also raise a BookingException for removing non-existing
# booking id.
    # def deleteBooking(self, bookingId):
    def deleteBooking(self, bookingId, aDate):
        booking = self.searchBooking(bookingId)
        if booking is not None:
            # today = datetime.now()
            flightDate = booking.flight.departureDate
            if aDate > flightDate:
                raise BookingException('Cannot delete a past flight')
            self._bookings.pop(bookingId)
        else:
            raise BookingException('Removing non-existing booking id')

def getInt(menu):
    while True:
        try:
            return int(input(f'{menu}'))
        except ValueError as e:
            print(f'Option Error, please re-enter')

def loadBooking(airline):

    try:
        tryLoadBooking(airline)
    except BookingException as e:
        print(f"{e}\n")

def tryLoadBooking(airline):

    filename = input("File name to be uploaded for batch booking: ")

    try:
        infile = open(filename, "r")
    except:
        raise BookingException("Unable to locate file for batch booking")

    try:
        for line in infile:

            parts = line.split(',')
            pid,name,ydob=parts[1],parts[2],int(parts[3])
            fno,destination,fare=parts[4],parts[5],float(parts[6])
            fyy,fmm,fd,fh,fmn=(int(x) for x in parts[7:12])
            byy,bmm,bd,bh,bmn=(int(x) for x in parts[12:17])

            p1 = Passenger(pid,name,ydob)
            
            fdate = datetime(fyy,fmm,fd,fh,fmn)
            f1 = Flight(fno,destination,fdate,fare)
            
            bdate = datetime(byy,bmm,bd,bh,bmn)

            if parts[0].strip() == "Individual":
                bk1 = IndividualBooking(p1, f1, bdate)
                airline.addBooking(bk1)
            elif parts[0].strip() == "Corporate":
                cname = parts[17].strip()
                bk1 = CorporateBooking(p1, f1, bdate, cname)
                airline.addBooking(bk1)
            else:
                raise BookingException("Unknown passenger type")
    finally:

        infile.close()

def getDate(message):
    while True:
        try:
            aDate = input(f"Plase enter year, month, day, hr, min of {message}: ")
            yy, mm, dd, hr, mn = (int(x) for x in aDate.split(','))
            return datetime(yy,mm,dd,hr,mn)
        except ValueError as e:
            print(f'The input is not valid')

def getFlight():
    fInfo = input("Please enter flight number, destination, fare of the flight: ")
    fnm, dest, fare = fInfo.split(',')
    fare = float(fare)
    dpDate = getDate('departure date')
    return Flight(fnm, dest, dpDate, fare)

def getPassenger():
    pInfo = input("Please enter passenger id, name, year of birth: ")
    pid, pname, yDob = pInfo.split(',')
    yDob = int(yDob)
    return Passenger(pid, pname, yDob)

def addBooking(airline):

    bktype = getInt('''Which type of booking
1. Individual Booking
2. Corporate Booking: ''')

    f = getFlight()
    p = getPassenger()
    bkd = getDate("booking date")
    # print(f,p,bkd)

    try:
        if bktype == 2:
            cname = input("Enter name of corporation: ")
            bk = CorporateBooking(p,f,bkd,cname)
            airline.addBooking(bk)
        else:
            bk = IndividualBooking(p,f,bkd)
            airline.addBooking(bk)
    except BookingException as e:
        print(e)
    except Exception as e:
        print(e)

def deleteBooking(airline):
    bkid = getInt(f"Enter booking id: ")
    try:
        today = datetime.now()
        airline.deleteBooking(bkid, today)
        print(f"Booking id={bkid} has been deleted")
    except BookingException as e:
        print(f"{e}\n\n")

def changeBooking(airline):
    bkid = getInt(f"The id of the booking to be changed: ")
    newFlight =getFlight()
    try:
        airline.changeBooking(bkid,newFlight)
        print(f"The booking id:{bkid} has been successfully changed")
    except BookingException as e:
        print(e)

if __name__ == "__main__":

    airline = Airline('Singapore Airline')

    while True:

        option = getInt('''Menu
1. Add Booking
2. Change Booking
3. Delete Booking
4. List Booking
5. Load Booking
6. Exit: ''')

        if option == 6:
            break
        elif option == 1:
            addBooking(airline)
            # To write to a file, pls refer to https://www.w3schools.com/python/python_file_write.asp 
        elif option == 2:
            changeBooking(airline)
        elif option == 3:
            deleteBooking(airline)
        elif option == 4:
            for key, value in airline.bookings.items():
                print(f"The booking with id:{key}\n{value}\n\n")
        elif option == 5:
            loadBooking(airline)
        else:
            print(f"Option not supported, please renter")

        print(option)

if __name__ == "__test__":

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

