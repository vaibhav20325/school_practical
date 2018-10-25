l=eval(input('Enter list '))
for i in range(1,len(l)):
    a=l[i]
    j=i-1
    while (a<l[j]) and j>-1:
        l[j+1]=l[j]
        j=j-1
    l[j+1]=a
print(l)
