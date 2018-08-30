d=int(input("Enter Day: "))
m=int(input("Enter Month: "))
y=int(input("Enter Year: "))
if m==1:
    month='JAN'
elif m==2:
    month='FEB'
elif m==3:
    month='MAR'
elif m==4:
    month='APR'
elif m==5:
    month='MAY'
elif m==6:
    month='JUN'
else:
    month=m
y=y%100
print(d,'-',month,'-',y)
