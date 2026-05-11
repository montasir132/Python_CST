# def triangle(a, b):
#     area = 0.5 *  a * b
#     return area
# a = float(input("Enter your height: "))
# b = float(input("Enter your base: "))
# result = triangle(a, b)
# print(f"triangle area = {result}")

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
res = triangle_area(a, b, c)
print(res)