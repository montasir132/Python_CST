# Function to Add five number For list 
def sum_list(numbers):
    sum = 0
    for num in numbers:
        sum+=num
    return sum
num_list = [10,20,30,40,50]
result = sum_list(num_list)
print("sum of list = ",result)