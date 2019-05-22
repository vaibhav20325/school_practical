key=int(input('Enter key: '))
f=open('q16.txt','r')
mode=input('Encode(e)/Decode(d):')
if  mode.lower()=='e':
    pass
elif mode.lower()=='d':
    key=-1*key
text=f.read()
f.close()
dict={}
for i in range(ord('a'),ord('z')+1):
    if i+key>ord('z'):
        dict[chr(i)]=chr(i+key-26)
    else:    
        dict[chr(i)]=chr(i+key)
for i in range(ord('A'),ord('Z')+1):
    if i+key>ord('Z'):
        dict[chr(i)]=chr(i+key-26)
    else:    
        dict[chr(i)]=chr(i+key)
f=open('output16.txt','w')
for i in list(text):
    if i in dict:
        f.write(dict[i])
    else:
        f.write(i)
f.close()
