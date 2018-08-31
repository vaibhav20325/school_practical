s1=input('string1:')
s2=input('string2:')
if s2.find(s1)==0:
    print('Prefix')
if (s2[::-1]).find(s1[::-1])==0:
    print('Postfix')


