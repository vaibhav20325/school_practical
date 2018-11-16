n=int(input('Enter '))
l=[n]
while n!=1:
    if n%2==0:
        n=int(n/2)
    else:
        n=3*n+1
    l.append(n)
print(l)
