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

    def add(x, y):  
   """This function adds two numbers"" 
   return x + y 
def subtract(x, y): 
   """This function subtracts two numbers""" 
   return x - y 
def multiply(x, y): 
   """This function multiplies two numbers""" 
   return x * y 
def divide(x, y): 
   """This function divides two numbers"""  
   return x / y  
# take input from the user  
print("Select operation.")  
print("1.Add")  
print("2.Subtract")  
print("3.Multiply")  
print("4.Divide")  
  
choice = input("Enter choice(1/2/3/4):")  
  
num1 = int(input("Enter first number: "))  
num2 = int(input("Enter second number: "))  
  
if choice == '1':  
   print(num1,"+",num2,"=", add(num1,num2))  
  
elif choice == '2':  
   print(num1,"-",num2,"=", subtract(num1,num2))  
  
elif choice == '3':  
   print(num1,"*",num2,"=", multiply(num1,num2))  
elif choice == '4':  
   print(num1,"/",num2,"=", divide(num1,num2))  
else:  
   print("Invalid input")  
