# Assignment 3: Write a program to add five numbers from a list using function

# Description: একটি লিস্টে পাঁচটি সংখ্যা থাকবে। Function ব্যবহার করে তাদের যোগফল বের করতে হবে।

# Using Function
def sum_list(numbers):
    sum = 0
    for num in numbers:
        sum+=num
    return sum
num_list = [10,20,30,40,50]
result = sum_list(num_list)
print("sum of list = ",result)


# Using Class
class SumList:
    def __init__(self, numbers):
        self.numbers = numbers
    def calculate(self):
        total = 0
        for num in self.numbers:
            total += num
        return total
num_list = [10, 20, 30, 40, 50]
sum_obj = SumList(num_list)
print("Sum of list =", sum_obj.calculate())
