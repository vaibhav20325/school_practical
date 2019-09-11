import urllib
a=urllib.request.urlopen('https://pythonforbeginners.com/')
f=open('downloaded.htm','w')
for i in a.readlines():    
    f.write(str(i))
    print(i)
f.close()
print('Headers:')
print(a.headers)
a.close()

