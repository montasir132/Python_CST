# Assignment 1: Write a program to calculate the area of a Triangle  using both a function and a class.

# Description: একটি প্রোগ্রাম লিখতে হবে যা একটি ত্রিভুজের ক্ষেত্রফল বের করবে। এখানে আমরা base এবং height ব্যবহার করব। Function এবং Class দুটো দিয়েই সমাধান দেখানো হবে।


# Using Function
def triangle_area(base, height):
    return 0.5 * base * height

base = float(input("Enter base: "))
height = float(input("Enter height: "))
result = triangle_area(base, height)
print("Triangle Area (Function):", result)


# Using Class
class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

base = float(input("Enter base: "))
height = float(input("Enter height: "))
total = Triangle(base, height)
print("Triangle Area (Class):", total.area())
