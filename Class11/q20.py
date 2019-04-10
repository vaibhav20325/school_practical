'''
Pascal's Triangle
'''
import math
n=int(input("Enter number of rows: "))
for i in range(0,n):
    print((n-i)*' ',end='')
    for j in range(0,i+1):
        print(int(math.factorial(i)/(math.factorial(j)*math.factorial(i-j))),end=' ')
    print()
    
    
    
    
