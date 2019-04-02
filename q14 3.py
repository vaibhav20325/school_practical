def sortl(l):
    return(l[2])

datalist=[]
f=open('data.txt','r')

for lines in f.readlines():
    lines=lines.strip()
    l=lines.split('\t')
    l=tuple(l)
    datalist.append(l)
print(datalist)
f.close()
datalist.sort(key=sortl)
for i in datalist:
    print(i)
    
 
