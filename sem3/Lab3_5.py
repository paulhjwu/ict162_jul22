# You are required to write a program that computes road tax for such vehicles. Write the
# following:

# a. Vehicle class
# It has a vehicle number and engine capacity. Besides the standard constructor and accessor methods, 

from abc import ABC, abstractmethod

class Vehicle(ABC):
    
    def __init__(self, vnum, cap):
        self._vnum = vnum
        self._capacity = cap

    @property
    def vnum(self):
        return self._vnum

    @property
    def capacity(self):
        return self._capacity
    
# it has a computeRoadTax method that returns the amount
# of road tax to pay. There is no implementation for this method yet. 

    def computeRoadTax(self):
        pass

# Include a str method that returns the road tax as well as the vehicle number and engine
# capacity

    def __str__(self):
        return f'V-Number: {self._vnum} Capacity: {self._capacity} Road Tax: {self.computeRoadTax()}'

# b. PassengerVehicle class
# This class inherits from the Vehicle class. It has owner and age of the person who
# owns the vehicle. 

class PassengerVehicle(Vehicle):

    def __init__(self, vnum, cap, owner, age):
        super().__init__(vnum, cap)
        self._owner = owner
        self._age = age

# Road tax for passenger cars is computed based on $1 per cc
# of the engine capacity. For owners who are 55 and above, a 10% discount is
# given. 

    def computeRoadTax(self):
        tax = self._capacity * 1 
        if self._age >= 55:
            tax -= tax * 0.1
        return tax
        
# The str method should print the owner’s detail before the vehicle’s details.

    def __str__(self):
        return f'Owner: {self._owner} Age: {self._age} ' + super().__str__()

# c. CommercialVehicle class
# This class inherits from the Vehicle class. It has company registration
# number(String) and maxLadenWeight as attributes. 

class CommercialVehicle(Vehicle):
    
    def __init__(self, vnum, cap, coy_reg, maxLW):
        super().__init__(vnum, cap)
        self._coy_reg = coy_reg
        self._maxLW = maxLW

# Road tax is computed based
# on $1 per cc if the maxLadenWeight(int) is 3 metric tonnes or below and $1.50
# per cc otherwise. 

    def computeRoadTax(self):
        if self._maxLW <= 3:
            return 1.0 * self._capacity
        else:
            return 1.5 * self._capacity

# The str method should print the company detail before the
# vehicle’s details.

    def __str__(self):
        return f'Company Registration Number : {self._coy_reg} ' + super().__str__()    

# d. Write an application to test the PassengerVehicle and CommercialVehicle class.
# Add 2 Passenger cars and 2 commercial cars to a list. Use a loop to display the
# road tax to pay for each vehicle.
# Indicate the statement in your code that exhibits polymorphism

if __name__ == "__main__":

    vlist = []
    # v1 = Vehicle(1, 2000)
    pv1 = PassengerVehicle(2, 2000, 'Peter', 56)
    pv2 = PassengerVehicle(5, 3000, "John", 40)
    # print(pv1)
    vlist.append(pv1)
    vlist.append(pv2)

    cv1 = CommercialVehicle(3, 2000, "COY1", 3.5)
    cv2 = CommercialVehicle(4, 3000, "COY2", 2)
    # print(cv1)
    vlist.append(cv1)
    vlist.append(cv2)

    for i in vlist:
        print(i)

    print()