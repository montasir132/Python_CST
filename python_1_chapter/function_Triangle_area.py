import math
def Triangle_area(a,b,c):
    if((a+b)>c and (b+c)>a and (c+a)>b):
        s=(a+b+c)/2
        return math.sqrt(s*(s-a)*(s-b)*(s-c))
    else:
        return None

a=int(input("enter a valu a= "))
b=int(input("enter a valu b= "))
c=int(input("enter a valu c= "))
res=Triangle_area(a,b,c)
if res is None:
    print("it is not a Triangle")
else:
    print("Triangle area",res)
