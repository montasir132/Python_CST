def sum_odd_number():
    sum = 0 
    for i in range(1,101,2):
        sum+=i
    return sum
result = sum_odd_number()
print("sum of odd number = ",result)