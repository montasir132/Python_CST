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
res = roots(a,b,c)
print(f"quadratic: {res}")