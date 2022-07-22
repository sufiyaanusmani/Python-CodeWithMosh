# Class: blueprint for creating new object
# Object: instance of a class

class Point:
    # static
    defaultColor = "red"

    def __init__(self, x, y):
        self.x = x
        self.y = y


    @classmethod
    def zero(cls):
        return cls(0, 0)


    def draw(self):
        print(f"Point ({self.x}, {self.y})")

    
    # redefining magic method
    def __str__(self):
        return f"({self.x}, {self.y})"

    
    def __eq__(self, other):
        return (self.x == other.x and self.y == other.y)


    def __gt__(self, other):
        return self.x > other.x and self.y > other.y


    def __add__(self, other):
        return(self.x+other.x, self.y+other.y)


point = Point(1, 2)
point.draw()
point.z = 10
print(isinstance(point, Point))

another = Point(3, 4)
another.draw()

print(point.defaultColor)
print(another.defaultColor)
print(Point.defaultColor)
Point.defaultColor = "blue"
print(point.defaultColor)


p2 = Point.zero()
p2.draw()

# Magic methods are those methods that are called automatically such as constructor
# __name__


print(another) # calls magic method __str__
print(str(another)) # calls magic method __str__
