# program to calculate factorial of a number
# Sabelo Dlamini
# 11 March 2024

def factorial(num):
    if type(num) is not int:
        return None
    if num < 0 :
        return None
    if num == 0:
        return 1
    
    return num * factorial(num-1)

# using a for loop
fact= 0
def factorial_for(num):
    if type(num) is not int:
        return None
    if num < 0 :
        return None
    
    for i in range(num+1):
        if i == 0:
            fact = 1
        else:
            fact = fact * i 

    return fact


print(factorial(5))
print(factorial_for(5))