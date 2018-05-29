n=int(input("Enter the number:"))
a=n
b=n
arm=0
i=0
while b>0:
    b=b//10
    i=i+1

while a>0:
    d=a%10
    a=a//10
    arm=arm+d**i
if arm==n:
    print ("The nummber is an armstrong")
else:
    print ("The number is not an armstrong")
