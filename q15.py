f=open('myfile.txt','r')
words=f.read().lower().split(' ')
d={}
for i in words:
    d[i]=words.count(i)
print(d)
f.close()
print('Total no. of words:',sum(d.values()))
print('No. of different words:',len(d.keys()))
maxocc=max(d.values())
print(maxocc)
for i in d:
    if d[i]==maxocc:
        print(i)
