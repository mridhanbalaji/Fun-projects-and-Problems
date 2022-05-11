from calendar import c
userValue = int(input("Enter Value Here:"))
a, b = 0, 1
fibonaccinumber =0

if userValue <= 0:
    print("Error")

else:
    for i in range (0, userValue):
        print(str(fibonaccinumber)) 
        fibonaccinumber = a + b
        a = b
        b = fibonaccinumber 
       
from math import inf


a = 3
b = 5
multiplevalues = range(0, float(inf))
Sum = 0

for i in range (0, 1000):
    Sum = a*multiplevalues + b*multiplevalues

print(Sum)
    
