# Assignment 8: Write a program using a class and function to Finding the root of a quadratic equation.

# Description: Quadratic equation 𝑎𝑥^2+𝑏𝑥+𝑐=0 এর root বের করতে হবে।


# Using Function
import math
def roots (a, b, c):
    d = b**2 - 4*a*c 
    if d == 0:
        x = -b/(2*a)
        return x
    elif d>0:
        x1 = (-b + math.sqrt(d))/(2*a)
        x2 = (-b - math.sqrt(d))/(2*a)
        return x1, x2
    else:
        return "it's not a quadratic"
a = int(input("enter you value a: "))
b = int(input("enter you value b: "))
c = int(input("enter you value c: "))
result = roots(a,b,c)
print(f"quadratic: {result}")


# Using Class
import math
class QuadraticEquation:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def roots(self):
        d = self.b**2 - 4*self.a*self.c
        if d == 0:
            x = -self.b / (2 * self.a)
            return f"One real root: {x}"
        elif d > 0:
            x1 = (-self.b + math.sqrt(d)) / (2 * self.a)
            x2 = (-self.b - math.sqrt(d)) / (2 * self.a)
            return f"Two real roots: {x1}, {x2}"
        else:
            return "It's not a quadratic with real roots"
a = int(input("Enter value a: "))
b = int(input("Enter value b: "))
c = int(input("Enter value c: "))
quad = QuadraticEquation(a, b, c)
print("Quadratic Roots:", quad.roots())

