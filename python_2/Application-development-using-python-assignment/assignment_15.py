# Assignment 15: Write a program using Regex to find/search a specific word within a string.

# Description: Regex ব্যবহার করে একটি string এর মধ্যে নির্দিষ্ট শব্দ খুঁজতে হবে।

import re
text = "Python is powerful and easy to learn."
pattern = r"powerful"

if re.search(pattern, text):
    print("Word found!")
else:
    print("Word not found!")
