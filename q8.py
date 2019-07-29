l1=[2,2,3,0]
l2=[2,2,3,0]

def merge(list1,list2, distinct = False):
    list3 = list1 + list2
    new_list=[]
    for i in list3:           
        if (i not in new_list) or not(distinct):
            for j in range(len(new_list)):
                if new_list[j] < i:
                    pass
                else:
                    new_list.insert(j,i)
                    break
            else:
                new_list.append(i)                
    return new_list

def commonSum(list1, list2):
    sum = 0
    for i in merge(list1,list2,distinct=True):
        if merge(list1,list2).count(i)>1:
            sum+=i
    return sum

def isCircular(list1,list2):
    cond=False
    for i in range(0,len(list1)):
        if list1[i:]+list1[0:i] == list2:
            cond=True
            break
    return cond

print(commonSum(l1,l2))
print(merge(l1,l2))
print(isCircular(l1,l2))
