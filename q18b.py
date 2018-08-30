n=int(input("Enter Number of terms: "))
b=0
sum=0
for j in range(1,n+1):
    b=j/((j+1)**(1/2))
    sum+=b
print(sum)
