# tuple => 8
# Concatination +
# repetition *
# membership in not in 
mytuple = (10,50,20,40,"montasir")
print("befor Concatination",mytuple)
mt=("Alam",10)
Concatination=mytuple+mt
print("after Concatination",Concatination)
repetition=mytuple*3
print("after repetition",repetition)
print(105 not in mytuple)

mttuple=(10, 50, 40, 2, 6, 4, 4)
print(mttuple)
print(max(mttuple))
print(min(mttuple))
print(any(mttuple)) #T/F
print(len(mttuple))
print(sum(mttuple))
print(mttuple.count(4))
print(sorted(mttuple))

# output
# befor Concatination (10, 50, 20, 40, 'montasir')
# after Concatination (10, 50, 20, 40, 'montasir', 'Alam', 10)
# after repetition (10, 50, 20, 40, 'montasir', 10, 50, 20, 40, 'montasir', 10, 50, 20, 40, 'montasir')
# True
# (10, 50, 40, 2, 6, 4, 4)
# 50
# 2
# True
# 7
# 116
# 2
# [2, 4, 4, 6, 10, 40, 50]