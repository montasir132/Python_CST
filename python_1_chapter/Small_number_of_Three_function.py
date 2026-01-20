# তিনটি সংখ্যার মধ্যে ছোট boro সংখ্যা নির্ণয়ের প্রোগ্রাম |

# Pogram-

def largest_number_of_three(a,b,c):
    if a>=b and a>=c:
        return a
    elif b>=a and b>=c:
        return b
    else:
        return c

def Smallest_number_of_three(a,b,c):
    if a<=b and a<=c:
        return a;
    elif b<=a and b<=c:
        return b
    else:
        return c

a=int(input("Enter a valu a= "))
b=int(input("Enter a valu b= "))
c=int(input("Enter a valu c= "))

largest=largest_number_of_three(a,b,c)
Smallest=Smallest_number_of_three(a,b,c)
print("largest number is= ",largest)
print("Smallest number is= ",Smallest)

# input-
# 47
# 99
# 72


# output-
# A = 47 is the smallest number