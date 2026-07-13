# Assignment 13: Write a program demonstrating Polymorphism.

# Description: Polymorphism এর উদাহরণ দিতে হবে।

class Bird:
    def fly(self):
        print("Birds can fly")

class Penguin(Bird):
    def fly(self):
        print("Penguins cannot fly")

def show_fly(bird):
    bird.fly()

b = Bird()
p = Penguin()

show_fly(b)
show_fly(p)
