class Rectangle:
    def __init__(self, length, width):
        self._length = length
        self._width = width
    
    @property
    def length(self):
        return self._length
    
    @length.setter
    def length(self, newLength):
        self._length = newLength

    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self, newWidth):
        self._width = newWidth

    def getArea(self):
        return self.length * self.width
    
    def getPerimeter(self):
        return 2 * (self.length + self.width)

    def increaseSize(self, deltaLength, deltaWidth):
        self._length += deltaLength
        self._width += deltaWidth

    def isBigger(self, rect):
        if self.getArea() > rect.getArea():
            return True
        return False

    def __str__(self):
        return f"Length: {self._length}, Width: {self._width}, Area: {self.getArea()}, Perimeter: {self.getPerimeter()}"
    
if __name__ == "__main__":

# It has the following methods:
#   getArea() that returns the area of the rectangle
#   getPerimeter() that returns the perimeter of the rectangle
#   increaseSize(deltaLength, deltaWidth) that increases the length and
#   width of the rectangle by deltaLength and deltaWidth respectively.
#   isBigger(rect) that has another rectangle as parameter. The method
#   returns True if the current area is bigger than the area of the rectangle
#   rect and False otherwise.
#   __str__() method that returns a string representation of a Rectangle
#   object, including its area and perimeter as in:
#   Length: 2.0 Width: 5.0 Area: 10.0 Perimeter: 14.0


    # r1 = Rectangle(2, 4)
    # r2 = Rectangle(3, 4)

    # print(r1.length)

    # r1.length = 4

    # r3 = Rectangle(2, 5)
    # print(r3.getArea())
    # print(r3.getPerimeter())
    
    # r3.increaseSize(1, 1)
    # print(r3.getArea())
    # print(r3.getPerimeter())

    # if r3.isBigger(r2):
    #     print("r3 is bigger")

    # print(r1)
    # print(r2)
    # print(r3)

# Test out the Rectangle class with the following statements:
# i. Create a Rectangle object r1 with any dimension.
    r1 = Rectangle(2,5)
# ii. Print the details of r1.
    print(r1)
# iii. Increase the size of the rectangle by 10 units on both sides.
    r1.increaseSize(10, 10)
# iv. Print the details of r1 again.
    print(r1)
# v. Create another rectangle r2 with any dimension.
    r2 = Rectangle(6, 8)
# vi. Print the area and perimeter using the getArea() and getPerimeter() methods.
    print(f"Area: {r2.getArea()}, Perimeter: {r2.getArea()}")
# vii. Compare r1 with r2 using the isBigger() method. Display the outcome.
    if r1.isBigger(r2):
        print(f"{r1} is bigger than {r2}")
    else:
        print(f"{r2} is bigger than {r1}")