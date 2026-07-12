# 1. Open() -> File Object = open("file name", "mode", "buffering")  
#   file modes: r -> read, w -> write, a -> append
# 2. Read() -> Reads the content of the file
# 3. Write() -> Writes content to the file
# 4. Close() -> Closes the file

file = open("myintro.txt", "w")  # Open the file in write mode
file.write("Hello, this is a sample text.\n")  # Write content to the file
file.write("This is the second line of the text.\n")  # Write another line
file.close()  # Close the file



# file should show in command prompt, if not then check the path of the file and run the code again
file = open("myintro.txt", "r")  # Open the file in read mode
content = file.read()  # Read the content of the file
print(content)  # Print the content
file.close()  # Close the file