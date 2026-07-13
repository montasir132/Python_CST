#Assignment 14: Write a program demonstrating exception handling (raising an exception).

# Description:Exception handling এর উদাহরণ দিতে হবে।

try:
    num = int(input("Enter a number: "))
    print("Result:", 10/num)
except ZeroDivisionError:
    print("Error: Division by zero!")
except ValueError:
    print("Error: Invalid input!")
