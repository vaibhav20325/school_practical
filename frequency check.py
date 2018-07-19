s=input("Enter ")
s=s.lower()
for i in range(97,123):
    if chr(i) in s:
        print (chr(i),":",s.count(chr(i)), end="  ")