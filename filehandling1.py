words=0
char=0
f=open('text.txt','r')
listl=f.readlines()
print('first line:',listl[0])
print('last line:',listl[-1])

for i in listl:
    if i[0]=='T':
        print(i)
for i in listl:
    l1=i.split()
    words=words+len(l1)
    l2=list(i)
    char=char+len(l2)
    print(i)
print('words:',words,'char:',char)

a,e,i,o,u=0,0,0,0,0

for j in listl:
    cnt=j.lower().count('a')
    a+=cnt
    cnt=j.lower().count('e')
    e+=cnt
    cnt=j.lower().count('i')
    i+=cnt
    cnt=j.lower().count('o')
    o+=cnt
    cnt=j.lower().count('u')
    u+=cnt
print('A:',a,'\n''E:',e,'\n''I:',i,'\n''O:',o,'\n''U:',u,'\n')
f.close()
