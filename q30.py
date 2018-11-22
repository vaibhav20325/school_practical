d={}
relatives={'Lisa':'daughter','Bart':'son','Marge':'mother','Homer':'father','Santa':'dog'}
ages={'Lisa':8,'Bart':10,'Marge':35,'Homer':40,'Santa':2}
for i in relatives:
    d[i]=([relatives[i],ages[i]])
print('The Simposons')
for i in d:
    print(i,'is a',d[i][0],'and is',d[i][1],'years old')
