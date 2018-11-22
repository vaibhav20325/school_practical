x=int(input("Enter rows "))
y=int(input("Enter columns "))
l=[]
for i in range(x):
    l.append([])
    for j in range (y):
        l[i].append(i*j)
for k in l:
    print(k)
