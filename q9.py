import numpy as np

array= (np.random.random(25)*5).round(1)
print(array.reshape((5,5)))
max=0
for i in array:
    if list(array).count(i)> max:
        max=i
print("Most frequently occuring:", max)
print('Maximum value is: ',np.max(array))
print('Minimum value is: ',np.min(array))

scaler=int(input('Enter Number: '))
closest=np.argmin(np.absolute(array-scaler))
print('CLosest element is: ',array[closest])
