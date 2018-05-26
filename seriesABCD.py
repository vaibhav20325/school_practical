
cnt=0
n=int(input("Enter number of rows: "))
for i in range(0,n,1):
    cnt=cnt + i
    print((n-i-1)*" ", end="")
    for j in range(cnt,i+1+cnt,1):
        print(chr(j%26+ord("A")), end=" ")
    print()
