n=int(input("Enter the number:"))
a=n**2
b=n
i=0
while b>0:
    b=b//10
    i=i+1
if a%(10**i)==n:
    print ("The nummber is automorphic")
else:
    print ("The number is not automorphic")
