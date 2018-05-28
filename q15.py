a=int(input("Enter First Number"))
b=int(input("Enter Second Number"))
while a!=b:
  if a>b:
    a=a-b
  else:
    b=b-a
print("The HCF is ",a)
