s=int(input("Enter Speed:"))
a=str(input("Is today your birthday? (yes/no) "))
if a=="yes":
    if s<=65:
        t=0
    elif s<=85:
        t=1
    else :
        t=2
elif a=="no":
    if s<=60:
        t=0
    elif s<=80:
        t=1
    else :
        t=2
else: t="error"
print ("The ticket number is ",t )
