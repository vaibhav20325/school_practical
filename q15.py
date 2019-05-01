f=open('myfile.txt','r')
words=f.read().lower().split(' ')
for i in range(len(words)):
    if not(words[i][0].isalnum()):
        words[i]=words[i][1:]
    if not(words[i][-1].isalnum()):
        words[i]=words[i][0:-1]
d={}
lendict={}
for i in words:
    d[i]=words.count(i)
print(d)
f.close()
print('Total no. of words:',sum(d.values()))
print('No. of different words:',len(d.keys()))
maxocc=max(d.values())
print('Most Common words:',end=' ')
for i in d:
    if d[i]==maxocc:
        print(i,end=' ')
print()
for i in words:
        if len(i) not in lendict:
            lendict[len(i)]=[]
        if i not in lendict[len(i)]:
            lendict[len(i)].append(i)
print(lendict)
        
def find_longest_word():
    print('Longest Words:',lendict[max(lendict.keys())])
find_longest_word()
def filter_long_words(n):
    l=[]
    for i in lendict:
        if i>n:
            l.extend(lendict[i])
    return l
n=int(input('Enter the req length:'))
print('Words Longer than ',n,':',filter_long_words(n))
f.close()
f=open('newfile.txt','w')
text=' '.join(filter_long_words(8))
f.write(text)
f.close()

