s=input("Enter String ").upper()
a=input("Enter 'E' to encrypt, 'D' to decrypt ")
try:
    b=int(input("Enter number of rotation"))
except:
    b=13
c=''

if a.upper()=='E':
    for i in range (0,len(s)):
        if s[i]!=' ':
            d=ord(s[i])+b
            if d>ord('Z'):
                d=(d-ord('Z'))%26 +ord('A')-1
            c+=chr(d)
        else:
            c+=' '

print(c)
