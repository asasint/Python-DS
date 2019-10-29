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

def recur_fibo(n):  
   if n <= 1:  
       return n  
   else:  
       return(recur_fibo(n-1) + recur_fibo(n-2))  
    
# take input from the user  
nterms = int(input("How many terms? "))  
# check if the number of terms is valid  
if nterms <= 0:  
   print("Plese enter a positive integer")  
else:  
   print("Fibonacci sequence:")  
   for i in range(nterms):  
       print(recur_fibo(i))  
