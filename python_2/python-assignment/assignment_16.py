# Assignment 16: Write a program using Regex to extract numbers from a string.

# Description: Regex ব্যবহার করে একটি string থেকে সংখ্যা বের করতে হবে।
    

import re

text = "My phone number is 12345 and my code is 678."
numbers = re.findall(r"\d+", text)
print("Extracted Numbers:", numbers)
