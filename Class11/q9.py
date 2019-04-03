n=int(input("Enter number of units: "))
if n<=100:
    a=40*n
elif n<=300:
    a=40*(100) + 50*(n-100)
else:
    a=40*(100) + 50*(200)+ 60*(n-300)
print ("Charge = ",(a+5000)/100)
