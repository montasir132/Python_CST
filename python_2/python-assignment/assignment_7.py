# Assignment 7: Write a program to generate the Fibonacci series using a function and class.

# Description: Fibonacci series generate করতে হবে। Function এবং Class ব্যবহার করতে হবে।

# Using Function
def fibonacci(n):
    series = [0, 1]
    for i in range(2, n):
        series.append(series[-1] + series[-2])
    return series
n = int(input("Enter the number of terms for Fibonacci series: "))
result = fibonacci(n)
print("Fibonacci (Function):", result)


# Using Class
class Fibonacci:
    def __init__(self, n):
        self.n = n

    def generate(self):
        series = [0, 1]
        for i in range(2, self.n):
            series.append(series[-1] + series[-2])
        return series

n = int(input("Enter the number of terms for Fibonacci series: "))
f = Fibonacci(n)
print("Fibonacci (Class):", f.generate())
