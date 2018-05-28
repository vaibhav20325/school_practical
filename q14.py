n=int(input("Enter the number:"))
a=n
rev=0
while a>0:
    d=a%10
    a=a//10
    rev=rev*10+d
if rev==n:
    print ("The nummber is a palindrome")
else:
    print ("The number is not a palindrome")
