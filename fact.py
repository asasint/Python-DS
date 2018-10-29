#Program to find factorial of a number
fact=1
def factorial(n):
    global fact
    if n>1:
        for i in range(1,n+1):
            fact=fact*i
        return fact
    elif (n==1 or n==0):
        print("Factorial is 1")
    else:
        print("Enter positive number")

