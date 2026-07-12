# tk=int(input("Enter your amount: "))
# if(tk>=1000):
#     print("khicce khabo")
# elif(tk>=500):
#     print("barger khabo")
# elif(tk>=100):
#     print("fuska khabo")
# else:
#     print("kisu khabo na")

import math 
a=int(input("enter a valu a= "))
b=int(input("enter a valu b= "))
c=int(input("enter a valu c= "))
d=(b**2)-(4*a*c)
if(d==0):
    x=(-b/(2*a))
    print("Roots is a real number",x)
elif(d>0):
    x1= ((-b+math.sqrt(d))/(2*a))
    x2= ((-b-math.sqrt(d))/(2*a))
    print("Roots is a Real number",x1,"and",x2)
else:
    print("Roots are imaginary")

# import math
# a=int(input("enter a valu a= "))
# b=int(input("enter a valu b= "))
# c=int(input("enter a valu c= "))
# if((a+b)>c and (b+c)>a and (c+a)>b):
#     s=(a+b+c)/2
#     area=math.sqrt(s*(s-a)*(s-b)*(s-c))
#     print("Triangle area",area)
# else:
#     print("it is not a Triangle")

# if(a>b and a>c):
#     print(a,"is largest number")
# elif(b>a and b>c):
#     print(b,"is largest number")
# else:
#     print(c,"is largest number")