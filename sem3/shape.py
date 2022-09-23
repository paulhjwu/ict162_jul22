# Seminar 3 Slide 21 to 27 
from abc import ABC, abstractmethod
from math import pi

class Shape(ABC):

    def __init__(self, length):
        self.__length = length
    
    @property
    def length(self):
        return self.__length

    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):

    def __init__(self, length, width):
        super().__init__(length)
        self.__width = width
    
    @property
    def width(self):
        return self.__width

    def area(self):
        return self.__width * super().length

class Circle(Shape):

    def __init__(self, radius):
        super().__init__(radius)
        
    @property
    def radius(self):
        return self.length

    def area(self):
        return pi * super().length ** 2

if __name__ == "__main__":

    r1 = Rectangle(10, 20)
    c1 = Circle(10)

    print(r1.area())
    print(c1.area())

    print()

