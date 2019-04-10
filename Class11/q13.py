isbn =int(input("Enter 10 digit isbn number:"))
check_d=isbn%10
sum=0
d=0
for i in range(10,1,-1):
   d=isbn%(10**i)//10**(i-1)
   sum=sum+(d*(11-i))
if sum%11==check_d:
    print("It is a valid isbn")
else:
    print("It is not a valid isbn")
