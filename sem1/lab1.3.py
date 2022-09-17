class Point:
    def __init__(self, x:float, y:float):
        self._x = x
        self._y = y
    
    @property 
    def x(self):
        return self._x

    @x.setter 
    def x(self, nX):
        self._x = nX

    @property
    def y(self):
        return self._y
    
    @y.setter 
    def y(self, nY):
        self._y = nY

    @y.setter
    def y(self):
        return self._y

    def move(self, dx, dy):
        self._x += dx
        self._y += dy
    
    def distanceTo(self, aPoint):
        return ( (self._x - aPoint.x)**2 + (self._y - aPoint.y)**2 ) ** 0.5

    def quadrant(self):
        if self._x * self._y == 0:
            return 0
        if self._x > 0:
            # x > 0
            if self._y > 0:
                # y > 0
                return 1
            else:
                # y < 0
                return 2
        else:
            # x < 0
            if self._y > 0:
                # y > 0
                return 4
            else:
                # y < 0
                return 3

    def __str__(self):
        return f"({self.x}, {self.y})"

if __name__ == "__main__":

# # It has the following methods:
# #  Getter and setter properties for x and y .
# #  A move(dx, dy) method that moves to (x+dx, y+dy)

# # A distanceTo(aPoint) method that returns the distance to another point
# # (x1, y1). The distance is calculated by this formula:

#     p1 = Point(0, 3)
#     p2 = Point(4, 0)
#     print(p1.distanceTo(p2))

# # A quadrant() method that returns the quadrant of the point as follows:

#     p3 = Point(1, -3)
#     print(p3.quadrant())

# # A __str__() method that returns the string value in this format: (x, y)

#     print(p3)

# i. Create a point object p1, at (5, 1)

    p1 = Point(5, 1)

# ii. Print the coordinates of p1

    print(p1)
    print(f"{p1} is in quadrant {p1.quadrant()}")

# iii. Move p1 by delta (5, -5)

    p1.move(5, -5)

# iv. Create another point p2 at (10 , -10)

    p2 = Point(10, -10)

# v. Print the distance between p1 and p2

    print(p1.distanceTo(p2))

# vi. Print the quadrants for p1 and p2

    print(f"{p1} is in quadrant {p1.quadrant()}")
    print(f"{p2} is in quadrant {p2.quadrant()}")