m=int(input('Enter number of rows '))
n=int(input('Enter number of columns '))
l=[]
dsum1,dsum2=0,0
csum=0
small=0
for i in range (m):
    l.append([])
    for j in range (n):
        num=int(input('Enter value '))
        l[i].append(num)
        if i==0 and j==0:
            small=l[i][j]
        elif l[i][j]<small:
            small=l[i][j]
for x in l:
    print(x,'\t',sum(x))
if m==n:
    for i in range(m):
        dsum1+=l[i][i]
        dsum2+=l[i][m-i-1]
for i in range (n):
    for j in range (m):
        csum+=l[j][i]
    print (csum,end=' ')
    csum=0
print()
print(dsum2,'\t',dsum1)
print("Smallest Number is ",small)
