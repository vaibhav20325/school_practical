l=[2,43,231,4345,3424,12,6346456754765]
for i in range(0,len(l)):
    for j in range(0,len(l)-i-1):
        if l[j]>l[j+1]:
            l[j],l[j+1]=l[j+1],l[j]
print(l)
