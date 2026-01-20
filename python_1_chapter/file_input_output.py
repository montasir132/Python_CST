# Writing data to a file
with open("myintro.txt","w") as file:
    file.write("Hi,I am Rafi\n")
    file.write("Hi,I am Rafi\n")
    file.write("Hi,I am Rafi\n")

#Reading date from the file
with open("myintro.txt","r") as file:
    content=file.read()
    print(content)
    
# output
# Hi,I am Rafi
# Hi,I am Rafi
# Hi,I am Rafi