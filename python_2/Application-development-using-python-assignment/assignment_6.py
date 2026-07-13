# Assignment 6: Write a program to write and read data to a file.

# Description: একটি ফাইলে কিছু ডাটা লিখতে হবে এবং পরে সেই ডাটা আবার পড়তে হবে।

# Writing to a file
with open("data.txt", "w") as f: # f = open("data.txt", "w")
    f.write("Hello, this is a test file.\nPython File Handling Example.")

# Reading from a file
with open("data.txt", "r") as f:
    content = f.read()
    print("File Content:\n", content)
