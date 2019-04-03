n=int(input("Enter Number of terms: "))
a=int(input("Enter first term: "))
b=0
sum=0
for j in range(1,n+1):
    b=(a**j)/j
    sum+=b
print(sum)
