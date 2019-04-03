n=int(input("Enter number "))
a=1
length=0
m=d=0
sum=0
product=1
while a<n:
    length+=1
    a=10*a

for j in range(length,0,-2):
    d=(n%10**j)//10**(j-1)
    sum=sum+d
print("The sum of odd positioned digits is",sum)

for j in range(length-1,0,-2):
    m=(n%10**j)//10**(j-1)
    product=product*m
print("The product of even positioned digits is",product)

print("Their sum is",sum+product)
