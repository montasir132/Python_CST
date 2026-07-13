# Assignment 10: Write a program to calculate the area of a Circle using both a function and a class.

# Description: একটি বৃত্তের ক্ষেত্রফল বের করতে হবে।

# Using Function
import math
def circle_area(radius):
    return math.pi * radius**2
r = int(input("Enter the radius of the circle: "))
print("Circle Area (Function):", circle_area(r))


# Using Class
import math
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2
r = int(input("Enter the radius of the circle: "))
c = Circle(r)
print("Circle Area (Class):", c.area())
