from datetime import datetime

class VehicleException(Exception):
    ''' Base exception class for Vehicle application '''

class WeekEndViolationException(VehicleException):
    
    def __init__(self, vehicle, dateSpotted, message):
        super().__init__(message)
        self._vehicle = vehicle
        self._dateSpotted = dateSpotted

    @property
    def vehicle(self):
        return self._vehicle

    @property
    def dateSpotted(self):
        return self._dateSpotted

class Vehicle:

    _speedLimit = 100

    def __init__(self, vehicleNumber, weekendCar):
        self._vehicleNumber = vehicleNumber
        self._weekendCar = weekendCar
        self._speed = 0

    @property
    def vehicleNumber(self):
        return self._vehicleNumber

    @property
    def speed(self):
        return self._speed

    def violation(self, dateSpotted):

        # https://www.w3schools.com/python/trypython.asp?filename=demo_datetime3

        if not self._weekendCar:
            return False
        if 0 <= dateSpotted.date().weekday() <= 4 \
            and 7 <= dateSpotted.hour < 21 \
            or dateSpotted.date().weekday() == 5 \
            and 7 <= dateSpotted.hour < 15:
            raise WeekEndViolationException(self, dateSpotted, 'Week end hours are violated!')
        return False 

    @speed.setter
    def speed(self, newSpeed):
        if newSpeed > type(self)._speedLimit:
            raise VehicleException(f'{newSpeed} exceed speed limit {type(self)._speedLimit}')
        self._speed = newSpeed
    
    def __str__(self):
        return f'Vehicle: {self._vehicleNumber} Weekend: {self._weekendCar} Current speed {self._speed}'


if __name__ == "__main__":

    vehicles = []
    vehicles.append(Vehicle(2, True))
    vehicles.append(Vehicle(5, False))
    vehicles.append(Vehicle(3, True))
    vehicles.append(Vehicle(4, False))

    for v in vehicles:
        try:
            print(v)
            v.speed = v.vehicleNumber * 25
            print('Speed pass, current speed {}'.format(v.speed))
            if not v.violation(datetime(2018, 9, 25, 7, 5)):
                print('No violation of weekEnd hours')
        except WeekEndViolationException as e:
            print(f'{e.vehicle} weekend violation on {e.dateSpotted:%#d %b %Y %H:%M}')
        except VehicleException as e:
            print('Speed fail:', e)
        finally:
            print()