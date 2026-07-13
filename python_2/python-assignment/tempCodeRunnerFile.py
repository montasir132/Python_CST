import math
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2
r = int(input("Enter the radius of the circle: "))
c = Circle(r)
print("Circle Area (Class):", c.area())