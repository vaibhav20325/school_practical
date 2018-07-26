num=float(input("Enter number in Decimal: "))
Dtype=str(input("Enter B for Binary, O for Octal, H for Hexadecimal: "))
n=int(num)
frac=num-n
a=''
b='.'
d=0
r=0.5
if num==0:
    a='0'
else:
    if Dtype=='B':
        while n!=0:
            d=n%2
            n=n//2
            a+=str(d)
        while r!=0:
            frac=frac*2
            r=frac-int(frac)
            b+=str(int(frac))
            frac=frac-int(frac)
    elif Dtype=='O':
        while n!=0:
            d=n%8
            n=n//8
            a+=str(d)
    elif Dtype=='H':
        while n!=0:
            d=n%16
            n=n//16
            if d>9:
                d=chr(ord('A')+d-10)
            a+=str(d)
    else:
        print("Error")
print(a[::-1]+b)
