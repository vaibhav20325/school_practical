a=int(input("Enter Range Beginning:"))
b=int(input("Enter Range Ending:"))
for i in range (a,b+1,1):
    if(i%7==0)and(i%5!=0):
        print(i, end=", ")
