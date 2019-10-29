# import complex math module  
import cmath  
a = float(input('Enter a: '))  
b = float(input('Enter b: '))  
c = float(input('Enter c: '))  
  
# calculate the discriminant  
d = (b**2) - (4*a*c)  
  
# find two solutions  
sol1 = (-b-cmath.sqrt(d))/(2*a)  
sol2 = (-b+cmath.sqrt(d))/(2*a)  
print('The solution are {0} and {1}'.format(sol1,sol2))

import numpy as np   
  
arr = [0, 30, 60, 90 ]   
print ("Input array : \n", arr)   
  
radval = np.radians(arr)   
print ("\n Radian value : \n", radval)   
