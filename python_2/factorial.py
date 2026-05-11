def factorial(n):
    if n==0 :
        return 1
    elif n<0:
        return "Oh no! you enter negative number plz try again"
    else:
        return n*factorial(n-1)
n = int(input("enter your positive number: "))
res = factorial(n)
print(f"the factorial of {n} is: {res}")
