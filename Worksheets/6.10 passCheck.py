d=sp=l=u=0
s=input("Enter Password ")
for i in range(len(s)):
        if s[i].isdigit():
            d=d+1
        elif s[i].islower():
            l=l+1
        elif s[i].isupper():
            u=u+1
        else:
            sp=sp+1
if d>=3 and sp>=2 and l>=2 and u>1 and len(s)>=8:
    print("Valid")
else:
    print("Not Valid")
