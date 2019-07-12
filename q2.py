def count(n):
    return('Length:'+str(len(str(n).strip(' '))))
def reverse(n):
    return('Reverse:'+str(n)[::-1])
def hasdigit(n):
    i=input('Enter digit: ')
    if i in str(n):
        return(True)
    else:
        return(False)
def show(n):
    s=''
    s+=str(n)+'='
    l=list(str(n))
    for i in range(len(l)):
        s+=str((int(l[i])*(10**(len(l)-i-1))))
        if i != len(l)-1:
            s+=' + '
    return(s)
num=int(input('Enter Number: '))
print(count(num))
print(reverse(num))
print(hasdigit(num))
print(show(num))
