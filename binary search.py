
l=[1,3,53245,23,12]
x=int(input("Enter number to be checked "))
l.sort()
a=0
while len(l)>0:
    a=len(l)//2
    if l[a]==x:
        print("The number is present ")
        break
    elif l[a]<x:
        l=l[a+1:len(l)]
    elif l[a]>x:
        l=l[0:a]
else:
    print("The number is not present ")
    
