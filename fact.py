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

import numpy as np    
    
import numpy.matlib    
    
print(numpy.matlib.zeros((3,3),int,'C')) 

import gzip
print(gzip.decompress(b'\x1f\x8b\x08\x00\x95\x10\xe0R\x02\xffSPP\xf0\xc9/KU\x80\x03\x10\x8f\x0bB\xa1c.l\x82dJ\xe0\xb0\x01\xe6\x02\x0cATa.T\xf7\x02\x00\xd9\x91g\x05\xc5\x00\x00\x00').decode('ascii'))
