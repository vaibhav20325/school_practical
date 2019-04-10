a=int(input("Enter Number:"))
for i in range(2,int(a**(1/2)+1)):
    if a%i==0:
        print("Not a prime")
        break
else:
    print("it is a prime")
