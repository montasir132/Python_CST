# Assignment 2: Write a program to Find Area of a Triangle (Heron’s Formula) using both a function and a class.

# Description: একটি প্রোগ্রাম লিখতে হবে যা একটি ত্রিভুজের ক্ষেত্রফল বের করবে। এখানে আমরা ত্রিভুজের তিনটি বাহুর দৈর্ঘ্য ব্যবহার করব। Function এবং Class দুটো দিয়েই সমাধান দেখানো হবে।

# Using Function
import math
def triangle_area(a, b, c):
    if (a+b>c) and (a+c>b) and (b+c>a):
        s = (a+b+c)/2
        area = math.sqrt(s * (s-a) * (s-b) * (s-c))
    else:
        area = f"it's not a triangle"
    return area

a = int(input("enter your value a: "))
b = int(input("enter your value b: "))
c = int(input("enter your value c: "))
result = triangle_area(a, b, c)
print(result)

# Using Class
import math
class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def is_valid(self):
        return (self.a + self.b > self.c) and (self.a + self.c > self.b) and (self.b + self.c > self.a)
    def area(self):
        if self.is_valid():
            s = (self.a + self.b + self.c) / 2
            area = math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
            return area
        else:
            return "It's not a valid triangle"

a = int(input("Enter side a: "))
b = int(input("Enter side b: "))
c = int(input("Enter side c: "))
result = Triangle(a, b, c)
print("Triangle Area:", result.area())
