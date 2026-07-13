# Assignment 9: Write a program using a function and class to solve find the largest number among three numbers.

# Description: তিনটি সংখ্যার মধ্যে সবচেয়ে বড় সংখ্যা বের করতে হবে।

# Using Function
def largest(a, b, c):
    return max(a, b, c)
a= int(input("Enter first number: "))
b= int(input("Enter second number: "))
c= int(input("Enter third number: "))
print("Largest (Function):", largest(a, b, c))


# Using Class
class LargestNumber:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def find(self):
        return max(self.a, self.b, self.c)
a= int(input("Enter first number: "))
b= int(input("Enter second number: "))
c= int(input("Enter third number: "))
largeSt = LargestNumber(a, b, c)
print("Largest (Class):", largeSt.find())
