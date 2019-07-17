num=0
def pascal(n):
    global num    
    if n>num:
        num=n
    if n==1:
        print((num-n)*' ',1)
        return([1])
    if n>1:
        
        row=[0]+pascal(n-1)
        newlist=[]
        for i in range(len(row)):
            newlist.append(row[i]+row[(i+1)%len(row)])
        print((num-n)*' ',end=' ')
        for i in newlist:
            print(i,end=' ')
        print()
        return(newlist)
        

pascal(5)
