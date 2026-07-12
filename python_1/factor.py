n=int(input("Enter your valu= "))
f=1
if n==1 or  n==0:
    print("the factorial is 1")
elif n<0:
    print("the factorial is not posible")
else:
    for i in range(1,n+1):
        f=f*i
    print("the factorial is",f)