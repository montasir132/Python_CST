import math
def circle(r):
    area= math.pi*r**2
    return area
r = float(input("enter your radius:"))
result = circle(r)
print(result)