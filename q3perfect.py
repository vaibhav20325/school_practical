def Generatefactors(n):
    factors=[]
    for i in range(1,n//2+1):
        if n%i==0:
            factors.append(i)
    factors.append(n)
    return(factors)

def isPrimeNo(n):
    if len(Generatefactors(n))==2:
        return True
    else:
        return False

def isPerfectNo(n):
    if sum(Generatefactors(n))==n*2:
        return True
    else:
        return False
