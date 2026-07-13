# Assignment 12: Write a program demonstrating Inheritance — using a Sub Class and Super Class.
# Description: Inheritance দেখাতে হবে।


class Animal:
    def sound(self):
        print("Animals make sounds")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

d = Dog()
d.sound()
