class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def getArea(self):
        print(self.length*self.breadth, "is area of rectangle")

class Square(Rectangle):
    def __init__(self, side):
        self.side = side
        Rectangle.__init__(self, side, side)
    def getArea(self):
        print(self.side*self.side, "is the area of square")


x = Square(4)
x.getArea()
r = Rectangle(2, 4)
r.getArea()