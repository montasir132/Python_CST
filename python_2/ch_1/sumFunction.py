# def sum(a,b):
#     c=a+b
#     return c
# print (sum(10,20))


# def sum():
#     a=int(input("enter valu a: "))
#     b=int(input("enter valu b: "))
#     v=a+b
#     print (v)
# sum()

# with open("test.txt","w") as file:
#     file.write("fkgderikfmdmg\nksfmri")

import math 
def roots(a,b,c):
    d=(b**2)-(4*a*c)
    if(d==0):
        x=(-b/(2*a))
        return x
    elif(d>0):
        x1= (-b+math.sqrt(d))/(2*a)
        x2= (-b-math.sqrt(d))/(2*a)
        return x1,x2
    else:
        return "Roots are imaginary"

a=int(input("enter a valu a= "))
b=int(input("enter a valu b= "))
c=int(input("enter a valu c= "))
result=roots(a,b,c)
print("Quadratic equation :",result)
