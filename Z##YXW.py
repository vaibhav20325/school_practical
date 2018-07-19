n=int(input("Enter number of rows "))
i=ord('Z')
for j in range(1,n+1):
    if j%2==0:
        print( j*'#')
    else:
        for z in range(0,j):
            print(chr(i), end='')
            i=i-1
            if i <ord('A'):
                i=i+26
        print()
