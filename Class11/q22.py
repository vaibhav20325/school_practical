s=str(input("Enter the string: "))
initial=''
stringTitle=''
rep=''
for i in s:
    if i in rep:
        continue
    rep+=i
    print (i,"=",s.count(i),',', end='')
print()
s=s.lower()
tempLen=maxLen=0
tempWord=maxWord=''
s=' '+s+' '
for i in range (len(s)-1):
    if s[i].isspace() and s[i+1].isalpha():
        if ' ' in s[i+1:len(s)-1]:
            initial+=s[i+1].capitalize()+' '
        else:
            initial+=s[i+1].capitalize()
            j=i
            while s[j+1]!=' ':
                j+=1
                initial+=s[j+1]
        tempLen=0
        tempWord=''
        stringTitle+=s[i+1].capitalize()
        while s[i+1]!=' ':
            i+=1
            tempLen+=1
            tempWord+=s[i]
            stringTitle+=s[i+1]
        if tempLen> maxLen:
            maxLen=tempLen
            maxWord=tempWord
print (maxLen,maxWord)
print(stringTitle)
print(initial)
