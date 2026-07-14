# Assignment 5: Write a program to calculate the sum of numbers from 1 to 100 using both a function and a class.

# Description: ১ থেকে ১০০ পর্যন্ত সংখ্যার যোগফল বের করতে হবে। Function এবং Class ব্যবহার করতে হবে।


# Using Function
def sum_1_to_100():
    return sum(range(1, 101))
print("Sum 1 to 100 (Function):", sum_1_to_100())


# Using Class
class SumNumbers:
    def __init__(self, start, end):
        self.start = start
        self.end = end
    def calculate(self):
        return sum(range(self.start, self.end+1))
s = SumNumbers(1, 100)
print("Sum 1 to 100 (Class):", s.calculate())



# ------ The following codes are not applicable for assignments. ------------

# Function to calculate sum of odd numbers from 1 to 100 
def sum_odd_number():
    sum = 0 
    for i in range(1,101,2):
        sum+=i
    return sum
result = sum_odd_number()
print("sum of odd number = ",result)
# Function to calculate sum of even numbers from 1 to 100
def sum_even_number():
    sum = 0 
    for i in range(2,101,2):
        sum+=i
    return sum
result = sum_even_number()
print("sum of even number = ",result)