a=eval(input('Enter numbers in  list '))
d={}
for i in a:
    d[i]=a.count(i)
for i in d:
    print(i,'\t','*'*d[i])
