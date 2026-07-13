# Assignment 4: Write a program to calculate the factorial of a number using both a function and a class.

# Description: একটি সংখ্যা দেওয়া হলে তার factorial বের করতে হবে। Function এবং Class দুটো দিয়েই সমাধান করতে হবে।


# Using Function
def factorial(n):
    if n == 0 or n == 1:
        return 1
    elif n<0:
        return "Oh no! you enter negative number plz try again"
    else:
        return n*factorial(n-1)
n = int(input("enter your positive number: "))
result = factorial(n)
print(f"the factorial of {n} is: {result}")


# Using Class
class Factorial:
    def __init__(self, n):
        self.n = n
    def calculate(self):
        if self.n == 0 or self.n == 1:
            return 1
        elif self.n < 0:
            return "Oh no! You entered a negative number, please try again."
        else:
            result = 1
            for i in range(1, self.n + 1):
                result *= i
            return result

n = int(input("Enter your positive number: "))
fact_obj = Factorial(n)
result_class = fact_obj.calculate()
print(f"(Class) The factorial of {n} is: {result_class}")
