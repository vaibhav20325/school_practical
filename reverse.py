a=int(input("Enter the number:"))

sum=0
rev=0
while a>0:
    d=a%10
    a=int(a/10)
    sum=sum+d
    rev=rev*10+d
print(sum)
print(rev)
