# Assignment 11: Write a program using a function and class to check whether a number is prime.

# Description: একটি সংখ্যা prime কিনা তা বের করতে হবে।

# Using Function
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
n = int(input("Enter a number to check if it is prime: "))
print("Prime (Function):", is_prime(n))


# Using Class
class PrimeCheck:
    def __init__(self, n):
        self.n = n
    def check(self):
        if self.n < 2:
            return False
        for i in range(2, int(self.n**0.5)+1):
            if self.n % i == 0:
                return False
        return True
n = int(input("Enter a number to check if it is prime: "))
p = PrimeCheck(n)
print("Prime (Class):", p.check())

