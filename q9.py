import numpy as np

array= np.random.randint(10, size=(5,5))
print(array)
print('Maximum value is: ',np.max(array))
print('Minimum value is: ',np.min(array))

scaler=int(input('Enter Number: '))
new_array=array-scaler
new_array=np.absolute(new_array)
print(new_array)
closest_diff=np.min(new_array)
for i in range(5):
    for j in range (5):
        if new_array[i][j]==closest_diff:
            print(array[i][j])

            
            
import numpy as np

array= np.random.randint(0,10,25)
print(array.reshape((5,5)))
print('Maximum value is: ',np.max(array))
print('Minimum value is: ',np.min(array))

scaler=int(input('Enter Number: '))
new_array=array-scaler
new_array=np.absolute(new_array)
print(new_array)

closest=np.argmin(new_array)
print(closest)
