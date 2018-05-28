a=int(input("Enter First Number "))
b=int(input("Enter Second Number "))
c=str(input("Enter Operator(+ - * /) "))
if c=="+":
    p=a+b
elif c=="-":
    p=a-b
elif c=="*":
    p=a*b
elif c=="/":
    p=a/b
else:
    p="Error"
print (p)
