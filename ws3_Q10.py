n=int(input("Enter: "))
low=101
low_n="0"
for i in range (n):
    n=str(input("Enter Name "))
    m=int(input("Enter Marks "))
    if m<low:
        low=m
        low_n=n
print (n)
