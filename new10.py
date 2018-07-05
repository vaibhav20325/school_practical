n=int(input("Enter number"))
a=1
i=0
sum=0
d=0
while a<n:
    i+=1
    a=10*a
print(i)
z=n
for j in range(i,0,-2):
    d=z//10**(j-1)
    z=z%10**(j-3)
    sum=sum+d
print(sum)
