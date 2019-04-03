def sortl(l):
    return(l[2])
d={}
datalist=[]
f=open('data.txt','r')
for lines in f.readlines():
    lines=lines.strip()
    l=tuple(lines.split('\t'))
    datalist.append(l)
f.close()
datalist.sort(key=sortl)
for i in datalist:
    print(i)
print('People with experience less than 3 yrs are:')   
for i in datalist:
    if int(i[2])<3:
        print(i[0])
    if i[3] not in d:
        d[i[3]]=0
        d[i[3]]+=1
print('Number of people acc to dept:')
for i in d:
    print(i,':',d[i])
